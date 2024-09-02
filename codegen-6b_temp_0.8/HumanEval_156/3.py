
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
    if 1 <= number <= 1000:
        roman = ''
        while number > 0:
            for numeral, value in ROW1:
                while number >= value:
                    roman += numeral
                    number -= value

        return roman.lower()
    else:
        raise ValueError("Argument must be between 1 and 1000 inclusive")

