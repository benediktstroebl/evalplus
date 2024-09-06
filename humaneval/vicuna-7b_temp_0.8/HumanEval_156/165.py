
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
    roman = []
    digits = 0
    while number > 0:
        digits += number % 10
        number //= 10
    for i in range(digits):
        roman.append(str(digits))
        digits -= i
    return ' '.join(roman[::-1])
