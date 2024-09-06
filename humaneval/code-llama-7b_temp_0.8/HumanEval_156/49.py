
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
    int_to_roman = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
    roman_to_int = dict([(v,k) for k,v in int_to_roman.items()])
    result = ''
    while number:
        for i in sorted(roman_to_int.keys(), reverse=True):
            while number >= i:
                result += int_to_roman[i]
                number -= i
    return result.lower()
