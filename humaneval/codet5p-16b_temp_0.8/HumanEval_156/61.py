
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

    M = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
    decimal_string = str(number)
    roman_string = []
    for i, val in enumerate(decimal_string):
        val = int(val)
        val_string = ""
        val_1 = val // 1000
        val_2 = (val % 1000) // 100
        val_3 = (val % 100) // 10
        val_4 = val % 10
        if val_1:
            val_string = val_string + "M" * val_1
        if val_2:
            val_string = val_string + "C" * val_2
        if val_3:
            val_string = val_string + "X" * val_3
        if val_4:
            val_string = val_string + "I" * val_4
        roman_string.append(val_string)
    return ''.join(roman_string)
