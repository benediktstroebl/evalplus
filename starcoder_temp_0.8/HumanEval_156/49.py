
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
    # Base case
    if number == 0:
        return ''

    roman_list = []

    # Recurse down to smaller numbers
    if number >= 10:
        roman_list.append(int_to_mini_roman(int(number/10)) + 'x')
        number %= 10
    if number >= 5:
        roman_list.append('v')
        number -= 5
    if number >= 1:
        roman_list.append('i' * number)

    # Concatenate and return
    return ''.join(roman_list)
