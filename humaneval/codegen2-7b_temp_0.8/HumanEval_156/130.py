
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
    if not isinstance(number, int) or number < 1 or number > 1000:
        raise ValueError("number must be an integer between 1 and 1000")

    if number == 1:
        return "i"

    mini_roman_str = ""
    while number > 0:
        if number % 100 > 0:
            mini_roman_str += lookup_table[number % 100] + lookup_table[int(number / 100)]
        else:
            mini_roman_str += lookup_table[number % 100]
        number = int(number / 100)

    return mini_roman_
