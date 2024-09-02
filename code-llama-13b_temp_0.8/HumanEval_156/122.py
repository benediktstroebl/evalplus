
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
    numerals = {
        1: "i",
        5: "v",
        10: "x",
        50: "l",
        100: "c",
        500: "d",
        1000: "m"
    }

    # numbers that are divisible by 5 but not 10, e.g. 5, 10, 50, 100, 500
    divisible_by_5 = {
        5: "v",
        10: "x",
        50: "l",
        100: "c",
        500: "d"
    }

    # numbers that are not divisible by 5 but are divisible by 10, e.g. 10, 50, 100
    divisible_by_10 = {
        10: "x",
        50: "l",
        100: "c"
    }

    # construct the result string by looping over the input
    result = ""
    for key in sorted(numerals.keys(), reverse=True):
        while number >= key:
            number -= key
            result += numerals[key]

            # if the number is now divisible by 5 but not 10
            if number in divisible_by_5:
                result = result[:-1] + divisible_by_5[number]
                number = 0

            # if the number is now divisible by 10
            if number in divisible_by_10:
                result = result[:-1] + divisible_by_10[number]
                number = 0

    return result.lower()

