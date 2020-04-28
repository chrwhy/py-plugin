

class Plugin2:

	def set_loader(self, loader):
		self.loader=loader

	def start(self):
		print('Plugin2 start')

	def run(self, something):
		print('Plugin2 running ', something)

	def stop(self):
		print('Plugin2 stop')


def get_class():
	return Plugin2