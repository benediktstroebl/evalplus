
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
    # get the result as a list, starting from the right
    result = []
    # while the number is greater than 0
    while number > 0:
        # if the number is equal to or less than 3:
        if number <= 3:
            # add the string equivalent of this number to the result
            result.append(_int_to_roman_string[number])
            # set the number to 0
            number = 0
        # else if the number is between 4 and 8:
        elif number <= 8:
            # add the string equivalent of this number to the result
            result.append(_int_to_roman_string[number])
            # set the number to 0
            number = 0
        # else if the number is equal to 9:
        elif number == 9:
            # add the string equivalent of this number to the result
            result.append(_int_to_roman_string[5])
            # set the number to 0
            number = 0
        # else if the number is between 10 and 40:
        elif number <= 40:
            # add the string equivalent of this number to the result
            result.append(_int_to_roman_string[5])
            # set the number to the modulus of the number minus 5
            number = number % 5
        # else if the number is between 41 and 50:
        elif number <= 50:
            # add the string equivalent of this number to the result
            result.append(_int_to_roman_string[1])
            # set the number to the modulus of the number minus 1
            number = number % 1
        # else if the number is between 51 and 90:
        elif number <= 90:
            # add the string equivalent of this number to the result
            result.append(_int_to_roman_string[5])
            # add the string equivalent of this number to the result
            result.append(_int_to_roman_string[1])
            # set the number to the modulus of the number minus 6
            number = number % 6
        # else if the number is between 91 and 100:
        elif number <= 100:
            # add the string equivalent of this number to the result
            result.append(_int_to_roman_string[
