from sense_hat import SenseHat
import time

sense= SenseHat()

white = (255, 255, 255)
red = (255, 0, 0)
orange = (255, 165, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
purple = (160, 32, 240)

while True:
    for event in sense.stick.get_events():
        if event.action =="pressed":
            if event.direction =="right":
                  sense.show_message("Hi, Lady", text_colour=blue, scroll_speed=0.05)
                  def show_t():
                    sense.show_letter("T", back_colour = red)
                    time.sleep(1)

                  show_t()
                  temperature = round(sense.temperature, 1)
                  sense.show_message("" + str(temperature) + " grados")

                  def show_h():
                    sense.show_letter("H", back_colour = blue)
                    time.sleep(1)

                  show_h()
                  humidity = round(sense.humidity, 1)
                  sense.show_message("" + str(humidity) + "% de humedad")


                  if temperature > 22 and humidity >= 40:
                      sense.show_message("Hace muy bueno, vete a dar un paseo. Sal de casa", text_colour=green)

                  elif temperature > 10 and temperature <= 22 and humidity > 10 and humidity < 39:
                      sense.show_message("No hace mucho frio. Deberias salir de casa", text_colour=green)

                  elif temperature > -15 and temperature <= 10 and humidity > 35 and humidity < 39:
                      sense.show_message("Brr, hace mucho frio. Ponte un buen abrigo", text_colour=blue)

                  elif temperature >= 100:
                      sense.show_message("Hace mucho calor, ¿Donde me has puesto?", text_colour=red)

                  elif temperature >= 35:
                      sense.show_message("La temperatura es muy alta, El cambio climatico esta afectando", text_colour=orange)
                      
                  elif temperature <= -15:
                      sense.show_message("La temperatura es muy baja! No salgas de casa", text_colour=white)
                  
                  sense.show_message("Have a nice day", text_colour=purple)
                  sense.clear()
