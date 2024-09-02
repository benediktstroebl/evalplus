
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
    if number < 1 or number > 1000:
        raise Exception("Error: number is not in the range [1, 1000]")
    if number < 1:
        return ''
    roman_num = []
    for i in range(1, number + 1):
        roman_num.append(mini_roman_mapping[i])
    return ''.join(roman_num
