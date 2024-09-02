
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
    roman_numeral = ""
    while number > 0:
        # If the input number is divisible by 1000, we can use the long form
        if number % 1000 == 0:
            roman_numeral += "M"
            number /= 1000
        # If the input number is divisible by 900, we can use the long form
        elif number % 900 == 0:
            roman_numeral += "CM"
            number /= 900
        # If the input number is divisible by 500, we can use the long form
        elif number % 500 == 0:
            roman_numeral += "D"
            number /= 500
        # If the input number is divisible by 400, we can use the long form
        elif number % 400 == 0:
            roman_numeral += "CD"
            number /= 400
        # If the input number is divisible by 100, we can use the long form
        elif number % 100 == 0:
            roman_numeral += "C"
            number /= 100
        # If the input number is divisible by 50, we can use the long form
        elif number % 50 == 0:
            roman_numeral += "XC"
            number /= 50
        # If the input number is divisible by 10, we can use the long form
        elif number % 10 == 0:
            roman_numeral += "X"
            number /= 10
        # If the input number is less than 10, we use the short form
        else:
            roman_numeral += str(number)
            number = number - number % 10
    return roman_numeral.lower()
