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
                  sense.show_message("" + str(temperature) + " degrees")

                  def show_h():
                    sense.show_letter("H", back_colour = blue)
                    time.sleep(1)

                  show_h()
                  humidity = round(sense.humidity, 1)
                  sense.show_message("" + str(humidity) + "% of humidity")


                  if temperature > 22 and humidity >= 40:
                      sense.show_message("That's quite warm, please wear a hat", text_colour=orange)
                      
                  elif temperature > 22 and temperature <35:
                      sense.show_message("That's quite warm, please wear a hat", text_colour=yellow)

                  elif temperature > 10 and temperature <= 22:
                      sense.show_message("Not too hot", text_colour=green)

                  elif temperature > -15 and temperature <= 10 and humidity > 35 and humidity < 39:
                      sense.show_message("Brr, it's chilly, climate change is here", text_colour=blue)

                  elif temperature >= 100:
                      sense.show_message("It's boiling, go inside", text_colour=red)

                  elif temperature >= 35:
                      sense.show_message("The temperature is extreme!, Please, stay at home.", text_colour=orange)
                        
                  elif temperature <= -15:
                      sense.show_message("The temperature is too low!, I think I am in the fridge", text_colour=white)
                  sense.show_message("Have a nice day", text_colour=purple)
                  sense.clear()
