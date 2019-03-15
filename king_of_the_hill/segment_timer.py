import RPi.GPIO as GPIO
from Adafruit_LED_Backpack import SevenSegment
from time import sleep


def setup():
    GPIO.setmode(GPIO.BCM)
    red_segment = SevenSegment.SevenSegment(address=0x70)
    green_segment = SevenSegment.SevenSegment(address=0x72)

    red_segment.begin()
    green_segment.begin()

    return red_segment, green_segment


def teardown():
    GPIO.cleanup()


def test_all_digits(segment):
    segment.clear()

    for num in range(9):
        segment.set_digit(0, num)
        segment.set_digit(1, num)
        segment.set_digit(2, num)
        segment.set_digit(3, num)

        sleep(0.5)


def main():
    try:
        red_segment, green_segment = setup()

        test_all_digits(red_segment)
        test_all_digits(green_segment)

    finally:
        teardown()


if __name__ == "__main__":
    main()
