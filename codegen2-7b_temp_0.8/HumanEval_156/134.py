
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
    if number < 1 or number > 1000:
        raise ValueError("num must be in range 1 <= num <= 1000")
    numeral = []
    for _ in range(number):
        numeral.append(chr(ord("i") + (number % 10 - 1)))
        number /= 10
    return "".join(numeral).lower()

