
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
    roman_chars = 'IVXLIIXCVII'
    numeral_chars = 'I V X L C D'
    result = ''
    for i in range(len(numeral_chars)):
        numeral = number // (2 ** (7 - i))
        if numeral <= 0:
            result += roman_chars[i]
            break
        else:
            result += numeral_chars[i] + roman_chars[i]
    return result.lower()
