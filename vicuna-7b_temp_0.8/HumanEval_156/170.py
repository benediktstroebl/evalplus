
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
    if number == 0:
        return 'i'
    if number == 1:
        return 'i'
    if number == 2:
        return 'ii'
    if number == 3:
        return 'iii'
    if number == 4:
        return 'iv'
    if number == 5:
        return 'v'
    if number == 6:
        return 'vi'
    if number == 7:
        return 'vii'
    if number == 8:
        return 'viii'
    if number == 9:
        return 'ix'

    # convert the number to its octal value
    octal_value = abs(int(number))

    # determine the roman numeral value of the octal value
    roman_value = {3: 'iii', 4: 'iv', 5: 'v', 6: 'vi', 7: 'vii', 8: 'viii', 9: 'ix'}
    roman_value[3] + octal_value

    # convert the octal value to a string
    roman_str = ''.join([roman_value[value] for value in octal_value])

    return roman_str.lower()
