
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
    s = ""
    number = abs(number)
    if number < 1 or number > 1000:
        return ""

    for i, num in enumerate(reversed(str(number)), 1):
        s += c[i] * int(num)
    return s.lower()

