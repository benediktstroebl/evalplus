
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
    roman_numeral = ''
    for i in range(10):
        numeral = number // i
        rem = number % i
        addend = [i] * (rem.count(i))
        roman_numeral += str(numeral) + addend[::-1]
        if i != 10:
            roman_numeral += 'I'
    return roman_numeral.lower()
