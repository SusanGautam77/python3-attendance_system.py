import RPi.GPIO as GPIO
import time
from mfrc522 import SimpleMFRC522
import board
import busio
import adafruit_character_lcd.character_lcd_rgb_i2c as character_lcd

# Initialize LCD
lcd_columns = 16
lcd_rows = 2
i2c = busio.I2C(board.SCL, board.SDA)
lcd = character_lcd.Character_LCD_RGB_I2C(i2c, lcd_columns, lcd_rows)

# Initialize RFID Reader
reader = SimpleMFRC522()

try:
    while True:
        # Clear LCD
        lcd.clear()

        # Display message on LCD
        lcd.message = "Place your card\non the reader."

        # Wait for card
        id, text = reader.read()

        # Clear LCD
        lcd.clear()

        # Display attendance message
        lcd.message = f"ID: {id}\nAttendance recorded."

        # Print ID to console
        print(f"ID: {id}")

        # Add your attendance handling logic here

        # Pause for a moment
        time.sleep(2)

except KeyboardInterrupt:
    GPIO.cleanup()
    lcd.clear()
    lcd.color = [0, 0, 0]  # Turn off LCD backlight
