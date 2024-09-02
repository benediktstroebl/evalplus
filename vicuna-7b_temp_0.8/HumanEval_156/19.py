
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
    numeral = str(number)
    result = ''
    for i in range(len(numeral)):
        if i % 2 == 0:
            result += numeral[i]
        else:
            digit = numeral[i]
            result += '_' + digit[1:]
            for j in range(1, len(digit)):
                result += 'A' + digit[j]
    return result.lower()
