

class Plugin1:

	def set_loader(self, loader):
		self.loader = loader

	def start(self):
		print('Plugin1 start')

	def run(self, something):
		print('Plugin1 running ', something)

	def stop(self):
		print('Plugin1 stop')


def get_class():
	return Plugin1