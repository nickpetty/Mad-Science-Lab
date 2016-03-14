# Sockets #
# - Panel Receive
# - Main Send
# - PTT
# - PWR
# - Data Recieve
# - Data Send
# - Voice Recieve
# - Audio Send

# Everything will have to be on different ports #
-------------------------------------------------
def panelRecieve():
	# listen for web data from panel and pass to serial write 1

def mainSend():
	# listen for serial data from main and pass to remote via web

def ptt():
	# listen for web data to trigger relay

def pwr():
	# listen for web data to trigger relay (pin to gnd)

def dataReceive():
	# listen for web data from remote com port and pass to serial write 2

def dataSend():
	# listen on com port 2 and relay to remote via web

def voiceRecieve():
	# listen to remote audio stream, pass out of sound card to main unit

def audioSend():
	# stream audio to remote device


def main():
	# create each socket in sub process as they are requested
	# remote connects back to host. Calling for a certain socket.  Socket is created and connection
	# is established.  remote then calls for another specific socket.