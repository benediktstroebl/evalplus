
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
    roman_chars = 'I X V I X L X I X V I'
    roman_num = []
    while number > 0:
        number, remainder = divmod(number, 100)
        if remainder >= 10:
            roman_num.append(roman_chars[remainder - 1])
        else:
            roman_num.append('0')
        number = remainder
    roman_num.reverse()
    return ''.join(roman_num)
