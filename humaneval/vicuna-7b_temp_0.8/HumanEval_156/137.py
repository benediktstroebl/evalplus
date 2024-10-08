
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
    roman_numerals = []
    while number > 0:
        remainder = number % 10
        number = number // 10
        roman_numerals.append(roman_numerals[-1] if remainder == 0 else f"{roman_numerals[-1]}-{remainder}")
    return ' '.join(roman_numerals[::-1])[::-1].lower()
