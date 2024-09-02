
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

    return ''.join([
        "m",
        "cm", "d", "cd", "c", "xc", "l", "xl", "x", "ix",
        "v", "iv", "i"
    ][number // 1000 * 4 + number // 100] +
        [
            "m",
            "cm", "d", "cd", "c", "xc", "l", "xl", "x", "ix",
            "v", "iv", "i"
        ][number // 100 - (number // 1000) * 10] +
        [
            "m",
            "cm", "d", "cd", "c", "xc", "l", "xl", "x", "ix",
            "v", "iv", "i"
        ][number // 10 - (number // 100) * 10] +
        [
            "m",
            "cm", "d", "cd", "c", "xc", "l", "xl", "x", "ix",
            "v", "iv", "i"
        ][number % 10 - (number // 10) * 10]
