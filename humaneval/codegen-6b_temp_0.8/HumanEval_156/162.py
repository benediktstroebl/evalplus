
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
    if not isinstance(number, int) or number < 1 or number > 1000:
        return 'Invalid Input'

    thousands = ['', 'M', 'MM', 'MMM']
    hundreds = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    tens = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    ones = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
    ans = ''

    while number > 0:
        ans = (thousands[number // 1000] + hundreds[number % 1000]) + (tens[number % 1000] + ones[number % 10])
        number //= 1000
        if number > 0:
            ans = (thousands[number // 1000] + hundreds[number % 1000]) + (tens[number % 1000] + ones[number % 10]) + ans
        number //= 1000

    return ans.lower()

