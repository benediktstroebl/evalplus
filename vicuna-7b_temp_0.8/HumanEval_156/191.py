
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
    roman = ''
    digit = str(number)
    if len(digit) == 1:
        roman = 'I'
    else:
        roman = digit[1]
        if len(digit) >= 2:
            digit = digit[:-1]
            value = int(digit)
            if value in [1, 4, 5, 9, 0]:
                roman = roman[1]
                if value == 4:
                    roman += 'CD'
                elif value == 0:
                    roman += 'XC'
                elif value in [1, 5]:
                    roman += 'D'
                else:
                    roman += 'C'
            elif value in [2, 6, 8]:
                roman = roman + value
                if value == 6:
                    roman += 'D'
                elif value == 8:
                    roman += 'C'
    return roman.lower()