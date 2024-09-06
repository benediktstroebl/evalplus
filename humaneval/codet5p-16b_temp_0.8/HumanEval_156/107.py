
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

    if 1 <= number <= 1000:
        result = ''
        value = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        symbol = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        n = [10, 100, 1000, 100000, 1000000]
        c = 1
        while number:
            for i in range(n[len(n) - 1]):
                if number - i >= 0:
                    result += symbol[symbol.index(result[len(result) - 1]) + 1]
                    number -= i
        return result.lower()
    else:
        return 'Enter a positive integer between 1 and 1000'
