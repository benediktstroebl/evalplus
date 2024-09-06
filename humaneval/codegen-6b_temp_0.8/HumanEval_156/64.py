
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
    if not 1 <= number <= 1000:
        raise ValueError("Integer must be between 1 and 1000.")
    mini_romans = {1: 'I', 5: 'V', 10: 'X', 50: 'L',
                   100: 'C', 500: 'D', 1000: 'M'}
    result = []
    while number > 0:
        for num, char in sorted(mini_romans.items(), reverse=True):
            while number >= num:
                result.append(char)
                number -= num
    return ''.join(result)

