
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
    d2r = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    r2d = {v: k for k, v in d2r.items()}

    res = ""
    for i, d in enumerate(reversed(str(number))):
        if i % 2:
            res += r2d[int(d)]
        else:
            if int(d) < 4:
                res += "".join([d2r[k] for k in r2d.keys() if r2d[k] < d2r[d]])
            else:
                res += d2r[d] + d2r[str(int(d) - 5)]
    return res.lower()

