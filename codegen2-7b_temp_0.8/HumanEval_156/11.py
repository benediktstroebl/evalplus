
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
    assert isinstance(number, int)
    assert 1 <= number <= 1000
    letters = ["", "m", "cm", "d", "cd", "c", "xc", "l", "xl", "x", "ix", "v", "iv", "i"]
    res = []
    while number > 0:
        for i in range(3):
            if number >= n_th_to_num[i]:
                res.append(letters[i])
                number -= n_th_to_num[i]
