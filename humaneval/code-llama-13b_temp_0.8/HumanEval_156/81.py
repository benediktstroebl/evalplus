
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
    assert number >= 1 and number <= 1000, 'Invalid number'

    romans = [
        (1000, 'm'),
        (500, 'd'),
        (100, 'c'),
        (50, 'l'),
        (10, 'x'),
        (5, 'v'),
        (1, 'i')
    ]

    def to_roman(num):
        result = ''
        for value, roman in romans:
            while num >= value:
                result += roman
                num -= value
        return result

    result = ''
    for index in range(len(romans)):
        if index == len(romans) - 1:
            result += to_roman(number)
            break
        else:
            (curr_value, curr_roman) = romans[index]
            (next_value, next_roman) = romans[index + 1]
            if number >= next_value:
                (curr_value, curr_roman) = romans[index + 1]
                result += to_roman(number - curr_value)
                break
            else:
                if curr_value <= number < next_value:
                    result += to_roman(number)
                    break

    return result.lower()

