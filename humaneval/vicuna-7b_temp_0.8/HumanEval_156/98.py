
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
    while number > 0:
        digits = number % 10
        number /= 10
        roman_numeral = (roman_numeral + (digits * (('x' if digits == 1 else ('i' if digits == 2 else ('v' if digits == 3 else ('l' if digits == 4 else ('c' if digits == 5 else ('d' if digits == 6 else ('b' if digits == 7 else ('a' if digits == 8 else ('vii' if digits == 9 else ('v' if digits == 10 else ''))))[digits - 1])))[::-1]))))[::-1]))[::-1]
    return roman_numeral.lower()
