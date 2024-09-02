
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
    # Roman numerals are based on the following key:
    # I: 1, V: 5, X: 10, L: 50, C: 100, D: 500, M: 1000

    int_to_roman = {
        1: "i",
        4: "iv",
        5: "v",
        9: "ix",
        10: "x",
        40: "xl",
        50: "l",
        90: "xlix",
        100: "xc",
        400: "cd",
        500: "d",
        900: "cm",
        1000: "m",
    }

    def _convert(num):
        if num < 1 or num > 1000:
            raise ValueError("Number must be between 1 and 1000")
        elif num in int_to_roman:
            return int_to_roman[num]
        else:
            last_digit = num % 10
            penultimate_digit = int((num % 100 - last_digit) / 10)
            if last_digit in int_to_roman:
                return int_to_roman[penultimate_digit] + int_to_roman[last_digit]
            elif penultimate_digit == 9:
                return "cm" + int_to_roman[last_digit]
            else:
                return int_to_roman[penultimate_digit] + "c" + int_to_roman[last_digit]

    return _convert(number).lower()

