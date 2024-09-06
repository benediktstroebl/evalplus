
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

    _m = {1:'i', 5:'v', 10:'x', 50:'l', 100:'c', 500:'d', 1000:'m'}
    _q = {1:1, 5:5, 10:10, 50:50, 100:100, 500:500, 1000:1000}
    _r = 'ivxlcdm'
    _z = _m.copy()
    _z[5] = 'v'
    _z[10] = 'x'
    _z[50] = 'l'
    _z[100] = 'c'
    _z[500] = 'd'
    _z[1000] = 'm'

    def _int_to_mini_roman(num):
        out = ''
        for q in _q.values():
            div, mod = divmod(num, q)
            if div:
                out += _m[q] * div
            num %= q
            if not num and div:
                break
        return out

    if number < 1:
        raise ValueError
    if number > 1000:
        raise ValueError

    a = _int_to_mini_roman(number)
    b = ''.join(map(lambda x: _z[x], map(int, list(a))))
    return b

