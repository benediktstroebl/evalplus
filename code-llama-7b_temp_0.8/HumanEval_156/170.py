
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
    roman_map = {1: 'i', 5: 'v', 10: 'x', 50: 'l', 100: 'c', 500: 'd', 1000: 'm'}
    roman_result = ''
    curr_digit = 1000
    while number > 0:
        if number // curr_digit > 0:
            times_digit = number // curr_digit
            if times_digit >= 9:
                roman_result += roman_map[curr_digit] * 9
            elif times_digit >= 5:
                roman_result += roman_map[curr_digit] * 5
            elif times_digit >= 4:
                roman_result += roman_map[curr_digit] * 4
                number -= curr_digit * 4
                curr_digit = curr_digit // 10
                continue
            elif times_digit >= 3:
                roman_result += roman_map[curr_digit] * 3
            elif times_digit >= 2:
                roman_result += roman_map[curr_digit] * 2
            elif times_digit >= 1:
                roman_result += roman_map[curr_digit]
            number -= curr_digit * times_digit
        curr_digit //= 10
    return roman_result.lower()

