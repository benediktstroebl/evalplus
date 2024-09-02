
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

    roman_numerals = {
        1: "i",
        5: "v",
        10: "x",
        50: "l",
        100: "c",
        500: "d",
        1000: "m",
    }

    result = []
    # Don't use 0 < num <= 1000, because that will exclude 1
    for n in range(0, 1000, 100):
        div, mod = divmod(number, n)
        if div == 4:
            result.append(roman_numerals[n] + roman_numerals[n * 5])
        elif div == 5:
            result.append(roman_numerals[n * 5])
        elif div > 5:
            result.append(roman_numerals[n * 5] + roman_numerals[n] * (div - 5))
        elif div > 0:
            result.append(roman_numerals[n] * div)

        if div > 1:
            number -= n * div

        if number == 0:
            break

    return "".join(result)

