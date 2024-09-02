
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
    roman_chars = 'I V X L C D MM'
    roman = ''
    for num in range(0, len(roman_chars), 2):
        val = number // (2 ** (len(roman_chars) - num))
        roman = roman + roman_chars[num] * val
    return roman.lower()
