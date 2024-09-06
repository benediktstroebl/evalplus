
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

    roman_dict = {
        1: "I",
        5: "V",
        10: "X",
        50: "L",
        100: "C",
        500: "D",
        1000: "M"
    }
    numeral = list(str(number))
    numeral.reverse()
    result = ""
    for i in numeral:
        if int(i) == 4:
            result += roman_dict[1000] + roman_dict[100]
        elif int(i) == 9:
            result += roman_dict[1000] + roman_dict[10]
        else:
            result += roman_dict[int(i) * int(i + 1) / 2]
    return result

