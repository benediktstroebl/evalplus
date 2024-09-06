
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
    roman = {}
    roman['M'] = 1000
    roman['CM'] = 900
    roman['D'] = 500
    roman['CD'] = 400
    roman['C'] = 100
    roman['XC'] = 90
    roman['L'] = 50
    roman['XL'] = 40
    roman['X'] = 10
    roman['IX'] = 9
    roman['V'] = 5
    roman['IV'] = 4
    roman['I'] = 1

    ans = []
    while number > 0:
        for key in roman.keys():
            if number >= roman[key]:
                ans.append(key)
                number -= roman[key]
                break

    return ''.join(ans)
