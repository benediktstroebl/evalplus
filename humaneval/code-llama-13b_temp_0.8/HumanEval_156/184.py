
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
        raise TypeError("number must be an integer")

    if number <= 0 or number >= 1000:
        raise ValueError("number must be between 1 and 1000 (inclusive)")

    roman_numeral = ""

    for i in range(3):
        power = 10**(2 - i)
        digit = number // power
        number %= power

        if digit == 9:
            roman_numeral += ("x" * (power // 10))
            roman_numeral += ("ix" * (power // 100))
        elif digit == 4:
            roman_numeral += ("iv" * (power // 10))
            roman_numeral += ("x" * (power // 100))
        elif 0 < digit < 5:
            roman_numeral += ("i" * digit)
        elif digit == 5:
            roman_numeral += ("v" * (power // 10))
        elif digit < 9:
            roman_numeral += ("v" * (power // 10))
            roman_numeral += ("i" * (digit - 5))
        elif digit == 10:
            roman_numeral += ("x" * (power // 10))

    return roman_numeral.lower()

