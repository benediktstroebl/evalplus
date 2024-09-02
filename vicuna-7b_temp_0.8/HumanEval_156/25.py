
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
    numeral = str(number)
    if numeral[0] == 'I':
        roman = 'I' + numeral[1:]
    else:
        numeral_map = [
            ['M', 'CM'], ['D', 'CD'], ['C', 'XC'], ['L', 'XL'],
            ['X', 'XX'], ['V', 'XV'], ['I', 'XI'], ['X', 'IX']
        ]
        numeral_list = []
        for num, unit in numeral_map:
            numeral_list.append(num + unit)
        numeral_list.reverse()
        while numeral_list:
            num, unit = numeral_list.pop()
            roman += num
            if numeral[0] == 'I':
                roman += 'I'
            elif unit == 'M':
                roman += 'MD'
            elif unit == 'C':
                roman += 'CD'
            elif unit == 'L':
                roman += 'XL'
            elif unit == 'X':
                roman += 'XX'
            else:
                roman += 'I'
    return roman.lower()