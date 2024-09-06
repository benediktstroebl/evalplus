
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
    # solution based on https://stackoverflow.com/a/3840009/3460717
    roman = {
        "1": "i", "4": "iv", "5": "v", "9": "ix",
        "10": "x", "40": "xl", "50": "l", "90": "xc",
        "100": "c", "400": "cd", "500": "d", "900": "cm",
        "1000": "M",
    }

    result = ""
    for key, value in roman.items():
        if key == "1000":
            result += value * (number // 1000)
            number -= (number // 1000) * 1000
        elif key in ("100", "10", "9", "50", "90", "40"):
            result += value * (number // int(key))
            number -= (number // int(key)) * int(key)
        elif key in ('4', '5', '6', '7', '8', '9'):
            result += value + key
    return result

