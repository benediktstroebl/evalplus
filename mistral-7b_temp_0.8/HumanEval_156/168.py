
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

    number_str = str(number)
    roman_str = ""

    if number == 0:
        return roman_str

    # The order of the numbers is important
    # Take the number from the last digit first
    for index in range(len(number_str) - 1, -1, -1):
        number_int = int(number_str[index])

        # At this point, number_int should be a one-digit number between 0 and 9

        if number_int == 0:
            continue

        elif number_int == 1:
            roman_str += "I"

        elif number_int == 2:
            roman_str += "II"

        elif number_int == 3:
            roman_str += "III"

        elif number_int == 4:
            roman_str += "IV"

        elif number_int == 5:
            roman_str += "V"

        elif number_int == 6:
            roman_str += "VI"

        elif number_
