
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
    # Ensure number is positive
    if number < 0:
        raise ValueError("Number must be positive")
    if number > MAX_ROMAN:
        raise ValueError("Integer is larger than highest roman numeral")
    # NOTE: The string of the roman numeral is kept identical to that of converting
    # the integer to roman numerals in RomanNumerals class. Thus, the same logic is
    # used here.
    digits = list(range(1, 10))
    digits_map = {}
    for count, value in enumerate(digits):
        digits_map[value] = count
    output = ""
    while number > 0:
        remainder = number % 10
        output += letters[remainder - 1]
        number = (number - remainder) / 10
    return output[::-1]

