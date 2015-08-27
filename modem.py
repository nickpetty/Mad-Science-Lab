
#handshake first, then transmit? ending with return ack confirming conformation on checksum check, or request for retransmit.

#transmitter

bufer=[]

def console(string):
	#convert string to byte string, add arguments. i.e., ACK, packet length, type, hex'string', checksum, ACKD; return packet.

	for bite in packet:
		transmitter(modem(bite).next())

def modem(bite):
	tones=[1,2,3,...]

	#encode bytes to audible freq. function here; return tone

	yield tone

def transmitter(tone):
	pyaudio.PyAudio.play(tone)



#receiver

def ear():
	#listen for ACK
	#record packet
	#check checksum
	#if checksum == good
		# transmit return ACK (special)
	#else
		# transmit retransmit rtsmt cmd

	#play each tone in the audio file (encoded(recorded) at a certain speed, decoded(played) at same speed) 
	# by only playing (i.e.) 1/24th/sec at a time and sending the tone to receiver().

def receiver(tone):
	#match tone to half/byte (maybe full byte with enough tones)
	#decode bytes
	#print message (or save file)

 #buffering only nessacary for full live stream and 'playback'. 
 #The other option is saving the file as it comes in THEN playing it back. 
 #SCRATCH - If there is a checksum, the checksum can not be verified for a live stream.  
 #Live stream would be too slow and even text would show up very slowly.