
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
    roman_numerals = {1: 'i', 5: 'v', 10: 'x', 50: 'l', 100: 'c', 500: 'd', 1000: 'm'}
    result = []
    for i in range(2, 10):
        # Add the special case for each number, e.g. 'ix' for '9'.
        # The other cases will be handled by the previous number.
        if i not in roman_numerals:
            result.append(roman_numerals[i])
    # Iterate over the number from the largest to the smallest.
    while number > 0:
        # For each roman numeral, check if it is smaller than the current number.
        # If it is, use it to subtract the number from the current number and add it to the result.
        for num in roman_numerals:
            if number >= num:
                result.append(roman_numerals[num])
                number -= num
                break
    return ''.join(result)

