import paramiko

class SSHC:

	def __init__(self, host, port, user, passw):
		self.hostssh = host
		self.portssh = port
		self.user = user
		self.passw = passw

	def check(self):
		sshpara = paramiko.SSHClient()
		try:
			sshpara.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			sshpara.connect(self.hostssh, self.portssh, self.user, self.passw)
			resp = sshpara.get_transport().is_alive()
			if str(resp) == 'True':
				return "Berhasil connect ke ssh!\nSSH aktif!"
		except:
			return "Gagal connect ke ssh!"


def detection(datassh):
	datasshnya2 = []
	datasshnya = datassh.split('@')
	for x in datasshnya:
		z = x.split(':')
		datasshnya2.append(z)
	forcheck = SSHC(datasshnya2[0][0], datasshnya2[0][1], datasshnya2[1][0], datasshnya2[1][1])
	print(forcheck.check())

def main():
	print('''
		SSH Checker
		https://github.com/ericgans
		''')
	print("Masukan dengan format sshhost:port@username:password")
	inputssh = input(" Masukan sshmu :  ")
	detection(str(inputssh))

if __name__ == __name__:
	main()
