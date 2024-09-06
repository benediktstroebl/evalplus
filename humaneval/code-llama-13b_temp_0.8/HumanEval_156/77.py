
def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    """

    # Map to hold the roman characters as the keys and their values
    roman_map = {
        1: "i",
        5: "v",
        10: "x",
        50: "l",
        100: "c",
        500: "d",
        1000: "m",
    }

    # Use a list to hold the roman string
    # We need a list because we'll be adding characters to it
    roman_string = []

    # Use a while loop to iterate through each digit of the input number
    # As long as there's a digit to the right of the current one, keep adding to the
    # number. For example: 152 --> 15 + 2
    while number > 0:
        # Find the units place by dividing by 10 until we reach the last digit
        # If the units place is 9 or above, we'll need to add the roman character
        # corresponding to the tens place to the units place, so we'll divide by 10
        # again until we get to 8 or below.
        # For example, for 152:
        #   units = 2 % 10 = 2
        #   tens = 2 // 10 = 0
        #   units = 0 % 10 = 0
        #   tens = 0 // 10 = 0
        #   units = 0 % 10 = 0
        #   tens = 0 // 10 = 0
        units = number % 10
        tens = number // 10
        # Keep dividing until we reach a digit of 9 or below
        while units >= 9:
            tens += 1
            units -= 10
        # Add the corresponding roman character to the string
        # For example, if we reach 152:
        #   tens = 1 and units = 5
        #   tens = 1 and units = 2
        #   tens = 15 and units = 2
        #   tens = 1 and units = 2
        #   tens = 1 and units = 2
       
