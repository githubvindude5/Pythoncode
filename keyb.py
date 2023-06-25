
import pyautogui
import time
time.sleep(3)
import random

def type_string_with_delay(string):
    for character in string:  # Loop over each character in the string
        pyautogui.write(character)  # Type the character
        delay = random.uniform(0, 0.1)  # Generate a random number between 0 and 10
        time.sleep(delay)  # Sleep for the amount of seconds generated

type_string_with_delay("Pythagoras theorem states that “In a right-angled triangle,  the square of the hypotenuse side is equal to the sum of squares of the other two sides“. The sides of this triangle have been named Perpendicular, Base and Hypotenuse. Here, the hypotenuse is the longest side, as it is opposite to the angle 90°. The sides of a right triangle (say a, b and c) which have positive integer values, when squared, are put into an equation, also called a Pythagorean triple. 1234567890, !@#$%^&*()_+")
