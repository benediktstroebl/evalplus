
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
    roman = ''
    factors = [1, 10, 50, 100, 500, 1000]

    for i in range(10):
        if number < factors[i]:
            roman = 'I' + roman
        else:
            remainder = number % i
            roman = i - (remainder if remainder != 0 else 0) + roman
            number = number // i

    return roman.lower()
