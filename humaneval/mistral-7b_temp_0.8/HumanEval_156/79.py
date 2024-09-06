
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
        raise ValueError("Input must be between 1 and 1000")

    ones_map = {'I': 1, 'V': 5, 'X': 10}
    tens_map = {'X': 10, 'L': 50, 'C': 100}
    hundreds_map = {'C': 100, 'D': 500, 'M': 1000}

    result = []
    for char in ones_map:
        for i in range(number // ones_map[char]):
            result.append(char)
            number -= ones_map[char]
        if number > 0:
            for char in tens_map:
                for i in range(number // tens_map[char]):
                    result.append(char)
                    number -= tens_map[char]
                if number > 0:
                    for char in hundreds_map:
                        for i in range(number // hundreds_map[char]
