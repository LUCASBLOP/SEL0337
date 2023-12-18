import RPi.GPIO as GPIO
from gpiozero import LED
from mfrc522 import SimpleMFRC522
from time import sleep

GPIO.setwarnings(False)

rled = LED(15)
gled = LED(18)

leitor = SimpleMFRC522()

print("Aproxime a tag do leitor para leitura.")

while True:
	id, texto = leitor.read()

	if id == 426883519919:
		print("Acesso liberado")
		rled.off()
		gled.on()
	else:
		print("Acesso negado")
		rled.on()
		gled.off()

	sleep(3)
	rled.on()
	gled.off()



