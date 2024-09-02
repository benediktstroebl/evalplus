
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

    assert number <= 1000, "Input number is greater than 1000"
    roman_map = [("", "M", 1000), ("CM", "DCCCC", 900), ("CD", "CCCC", 400), ("XC", "LXXXX", 90),
                 ("XL", "XXXX", 40), ("IX", "VIIII", 9), ("IV", "IIII", 4)]
    result = []

    for numeral, letters, value in roman_map:
        while number >= value:
            result.append(letters)
            number -= value
    return "".join(result)
