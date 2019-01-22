from subprocess import Popen, PIPE
import os, time

sh = lambda cmd: Popen(cmd,stdout=PIPE,shell=True).communicate()[0].strip()

read = lambda: sh("xsel -b").decode()
write = lambda x: os.system("echo -n \"%s\" | xsel -b" % x)

def fdecode(x):
	try:
		return x.decode()
	except:
		return str(x)[2:-1]

class ClipShell(object):
	def __init__(self, read=read, write=write, sh=sh):
		self.read = read
		self.write = write
		self.sh = sh

	def on_change(self, data):
		if data.startswith("clipshell::"):
			cmd = data[11:]
			res = fdecode(self.sh(cmd))
			self.write(res)

	def run(self, wait=0):
		old = ""
		while True:
			time.sleep(wait)
			new = self.read()
			if not old == new:
				self.on_change(new)
				old = new

ClipShell().run() if __name__ == "__main__" else None