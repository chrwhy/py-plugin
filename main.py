import os


class PluginLoader:

	def __init__(self):
		self.plugins = []
		self.load_plugins()

	def load_plugins(self):
		print("Loading plugins...")
		for filename in os.listdir("plugins"):
			if not filename.endswith(".py") or filename.startswith("_"):
				continue
			print(filename)
			self.run_plugin(filename)

	def reload_plugins(self):
		self.plugins = []
		self.load_plugins(self)

	def run_plugin(self, filename):
		print("Running plugin: %s", filename)
		plugin_name = os.path.splitext(filename)[0]
		plugin = __import__("plugins." + plugin_name, fromlist=[plugin_name])
		plugin_clz = plugin.get_class()
		plugin_instance = plugin_clz()
		plugin_instance.loader = self
		print('Plugin class: ', plugin_clz)
		plugin_instance.start()
		self.plugins.append(plugin_instance)

	def stop(self):
		for plugin in self.plugins:
			plugin.stop()

if __name__ == "__main__":
	plugin_loader = PluginLoader()
	for plugin in plugin_loader.plugins:
		plugin.run('testing...')

	plugin_loader.stop()

