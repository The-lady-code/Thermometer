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
                      sense.show_message("Hace mucho calor, apaga la calefaccion", text_colour=yellow)
                      
                  elif temperature > 10 and temperature <= 22 and humidity > 10 and humidity < 39:
                      sense.show_message("No hace mucho frio", text_colour=green)

                  elif temperature > -15 and temperature <= 10 and humidity > 35 and humidity < 39:
                      sense.show_message("Brr!, hace frio!, enciende la calefaccion", text_colour=blue)

                  elif temperature >= 100:
                      sense.show_message("Hace un calor espantoso, ¿Estoy en el horno?", text_colour=red)

                  elif temperature >= 35:
                      sense.show_message("La temperatura es muy alta!, ¿Que estas haciendo con la calefaccion?.", text_colour=orange)
                        
                  elif temperature <= -15:
                      sense.show_message("La temperatura es muy baja!, ¿Que estas haciendo con la calefaccion?.", text_colour=white)
                  sense.show_message("Que tengas un buen dia", text_colour=purple)
                  sense.clear()
