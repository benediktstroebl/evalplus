
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

    # We'll convert the number to a string
    num_str = str(number)
    # We'll build the roman numeral starting at the end of the string,
    # first working with the units (10^0), then tens (10^1), then hundreds (10^2),
    # and finally thousands (10^3)
    # To build the roman numeral, we'll start with the highest digit, and then work our way
    # down to the lowest
    roman_num = ""

    # We'll loop over the digits, from highest to lowest
    for i in range(len(num_str) - 1, -1, -1):
        # The highest digit is the unit
        if i == len(num_str) - 1:
            digit = num_str[i]
            # Since the highest digit is a unit, we'll build the roman numeral
            # with one, five, or ten
            if digit == "1":
                roman_num = roman_num + "i"
            elif digit == "5":
              
