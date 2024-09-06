
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
    assert isinstance(number, int) and 1 <= number <= 1000, "Bad arg: number"
    if number < 40:
        return TO_ROMAN[number]
    elif number < 500:
        a = divmod(number, 10)
        return TO_ROMAN[a[0] * 10] + int_to_mini_roman(a[1])
    elif number < 900:
        b = divmod(number, 100)
        return TO_ROMAN[b[0] * 100] + \
            TO_ROMAN[b[1] * 10] + int_to_mini_roman(b[2])
    elif number < 1000:
        c = divmod(number, 1000)
        return TO_ROMAN[c[0]] + TO_ROMAN[c[1] * 1000]
