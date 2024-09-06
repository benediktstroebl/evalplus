
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
    roman_characters = ['', 'i', 'v', 'x', 'l', 'c', 'd', 'm']
    roman_values = [1, 5, 10, 50, 100, 500, 1000]

    result = []
    for i in range(len(roman_characters)):
        while number >= roman_values[i]:
            result.append(roman_characters[i])
            number -= roman_values[i]

    return ''.join(result)

