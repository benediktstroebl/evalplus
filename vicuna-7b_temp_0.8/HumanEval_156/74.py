
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
    if number == 1:
        roman.append('I')
    elif number > 1 and number <= 99:
        numerator = number
        denominator = 10
        while denominator != 0:
            numerator /= denominator
            denominator = denominator // 10
        numerator_str = str(numerator)
        if denominator == 10:
            roman.append(numerator_str[0])
        else:
            roman.append(numerator_str[0])
            roman.append(numerator_str[1])
        if numerator_str[1] == '1':
            roman.append('A')
        else:
            roman.append('a')
    else:
        numerator = number // 1000
        denominator = number % 1000
        numerator_str = str(numerator)
        if denominator == 1000:
            roman.append(numerator_str[0])
        else:
            roman.append(numerator_str[0])
            roman.append(numerator_str[1])
            roman.append(numerator_str[2])
            if numerator_str[2] == '1':
                roman.append('A')
            else:
                roman.append('a')
    return ''.join(roman)
