
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
    for i in range(1000):
        if number >= i:
            roman.append(chr(i + 1))
            break
    else:
        roman.append(chr(900))
    roman_str = ''.join(roman)
    if number < 1000:
        return roman_str[0] + roman_str[1:].lower()
    else:
        return ''.join(roman_str[2:].lower())
