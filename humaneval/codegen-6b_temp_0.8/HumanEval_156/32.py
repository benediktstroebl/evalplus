
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
    if not isinstance(number, int):
        raise TypeError("int_to_mini_roman() only accepts integers, not %s" % type(number))
    if number < 1:
        raise ValueError("int_to_mini_roman() only accepts positive integers, not %d" % number)
    if number > 1000:
        raise ValueError("int_to_mini_roman() only accepts integers between 1 and 1000, not %d" % number)
    roman_str = ''
    while number > 0:
        if number >= 100:
            roman_str += 'c'
            number -= 100
        elif number >= 10:
            roman_str += 'd'
            number -= 10
        elif number == 9:
            roman_str += 'ix'
            number -= 9
        elif number >= 5:
            roman_str += 'v'
            number -= 5
        elif number >= 4:
            roman_str += 'iv'
            number -= 4
        elif number >= 1:
            roman_str += 'i'
            number -= 1
    return roman_str.lower()

