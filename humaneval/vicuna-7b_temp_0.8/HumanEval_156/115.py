
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
    roman_chars = 'IVXLCDM'
    result = []
    for i in range(len(str(number))):
        if number >= 1000:
            result.append(roman_chars[i])
        elif number >= 100:
            result.append(roman_chars[i-1])
        elif number >= 10:
            result.append(roman_chars[i-2])
        elif number >= 1:
            result.append(roman_chars[i-3])
        else:
            result.append(roman_chars[i-4])
    result = ''.join(result)
    return result.lower()
