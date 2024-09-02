
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

    digits = {
        1: "i",
        5: "v",
        10: "x",
        50: "l",
        100: "c",
        500: "d",
        1000: "m",
    }

    number = str(number)
    result = ""

    # delete all the 0s
    number = number.replace("0", "")

    for i in range(0, len(number), 3):
        triplet = int(number[i : i + 3])
        triplet_string = ""
        if triplet >= 1000:
            triplet_string += digits[1000] * int(triplet / 1000)
        if triplet % 1000 != 0:
            triplet_string += digits[100] * int(triplet % 1000 / 100)
        if triplet % 100 != 0:
            triplet_string += digits[10] * int(triplet % 100 / 10)
        if triplet % 10 != 0:
            triplet_string += digits[1] * (triplet % 10)
        result += triplet_string
    return result.lower()

