
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
    #The mini Roman numerals
    #"I" (1), "V" (5), "X" (10), "L" (50), "C" (100), "D" (500), "M" (1000)
    #Do not worry about the "IIII" and "XXXX" and "VIIII" etc.
    #You can use upper case as well to do it
    roman_numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    string = ""

    while number != 0:
        if number < 4:
            string += roman_numbers[str(number)]
            number = 0
        else:
            string += roman_numbers[str(number)]
            number -= 4

    return string
