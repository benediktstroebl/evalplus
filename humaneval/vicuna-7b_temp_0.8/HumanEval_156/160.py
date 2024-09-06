
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
    for i in range(len(str(number))):
        roman_digit = str(number // (10**(i+1)))
        roman.append(roman_digit[0])
        if len(roman_digit) > 1:
            roman_digit = roman_digit[:-2] + ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'][roman_digit.index('a')]
        else:
            roman_digit = 'a'
        roman.append(roman_digit)
    return ''.join(roman[::-1])