
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
    roman = []
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(0, len(str(number)), 3):
        digit = digits[number[i] - 2]
        roman.append(str(digit))
    roman_str = "".join(roman)
    return roman_str.lower()
