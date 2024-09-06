
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
    numeral_length = len(numeral)
    if numeral_length == 1:
        numeral = 'I' + numeral
    else:
        numeral = numeral[:2] + 'V' + numeral[2:]

    roman_length = 4
    roman = ''
    for i in range(numeral_length):
        digit = numeral[i]
        if digit >= 'A' and digit <= 'F':
            digit -= 9
            roman += 'V' if i < numeral_length - 1 else 'I'
            roman += chr(digit + 27 + 97)
        elif digit >= '0' and digit <= '8':
            digit -= 9
            roman += 'V' if i < numeral_length - 1 else 'I'
            roman += chr(digit + 27 + 97)
        else:
            roman += chr(digit + 122 + 97)
    return roman[::-1]
