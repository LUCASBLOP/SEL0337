import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
GPIO.setwarnings(False)
leitor = SimpleMFRC522()
texto = "12803370"
print("Aproxime a tag do leitor para leitura")
leitor.write(texto)
print("Concluido!")


