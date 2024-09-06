
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
    number = int(number)
    if 1 <= number <= 10:
        return [1, 5, 10][number - 1]

    elif 11 <= number <= 100:
        tens, remainder = divmod(number, 10)
        if remainder == 0:
            return [10, 100][tens - 1]
        else:
            return [tens, 10][tens - 1] + int_to_mini_roman(remainder)

    elif 101 <= number <= 1000:
        hundreds, tens = divmod(number, 100)
        if hundreds == 9:
            return 'cm'
        if hundreds == 4:
            return 'cd' + int_to_mini_roman(tens)
        else:
            return int_to_mini_roman(hundreds) + 'c' + int_to_mini_roman(tens)

    else:
        raise ValueError("The input is too large or negative.")

