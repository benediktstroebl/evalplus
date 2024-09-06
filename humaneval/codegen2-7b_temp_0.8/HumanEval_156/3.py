
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
    if not isinstance(number, int) or number < 0 or number > 1000:
        raise ValueError("Argument must be a positive integer")
    roman_numerals = ["", "i", "ii", "iii", "iv", "v", "vi", "vii"]
    result = ""
    while number > 0:
        if number >= 1000:
            result += roman_numerals[10]
            number -= 1000
        else:
            result += roman_numerals[number]
            number -= number
