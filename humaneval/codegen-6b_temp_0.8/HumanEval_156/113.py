
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
    dic = {1:'i', 5:'v', 10:'x', 50:'l', 100:'c', 500:'d', 1000:'m'}
    res = ''
    for i, val in enumerate(reversed(sorted(dic))):
        res += dic[val] * int(number / val)
        number %= val
    return res
    pass

