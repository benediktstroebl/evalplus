
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
    numeral_dict = {1000: "m", 500: "d", 100: "c", 50: "l", 10: "x", 5: "v", 1: "i"}
    roman_num = ""
    while number:
        for i in [1000, 500, 100, 50, 10, 5, 1]:
            if number >= i:
                roman_num += numeral_dict[i]
                number -= i
                break
    return roman_num.lower()

