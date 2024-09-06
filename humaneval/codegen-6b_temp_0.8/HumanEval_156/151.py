
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
    results = ""
    if number > 1000:
        raise ValueError("int_to_mini_roman: num too large")
    if number < 1:
        raise ValueError("int_to_mini_roman: num too small")
    if number == 1:
        return "i"
    if number == 2:
        return "ii"
    if number == 3:
        return "iii"
    if number == 4:
        return "iiii"
    if 5 <= number <= 8:
        return "v" + "iv" * (number - 5)
    if 9 <= number <= 40:
        return "v" + "vi" * (number % 10)
    if 41 <= number <= 99:
        return "v" + "vii" * (number % 10)
    if 100 <= number <= 499:
        return "v" + "viii" * (number % 10)
    if 500 <= number <= 999:
        return "v" + "ix" * (number % 10)
    if 1000 <= number <= 1999:
        return "v" + "x" * (number % 10)
    if 2000 <= number <= 3999:
        return "v" + "x" * (number % 10)
    if 4000 <= number <= 4999:
        return "v" + "x" * (number % 10)
    if 5000 <= number <= 5999:
        return "v" + "x" * (number % 10)
    if 6000 <= number <= 6999:
        return "v" + "x" * (number % 10)
    if 7000 <= number <= 7999:
        return "v" + "x" * (number % 10)
    if 8000 <= number <= 8999:
        return "v" + "x" * (number % 10)
    if 9000 <= number <= 999999:
        return "v" + "x" * (number % 10)
    if number == 1000:
        return "v" + "x" * 10

