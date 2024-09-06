
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

    roman_values = {
        1: "i",
        5: "v",
        10: "x",
        50: "l",
        100: "c",
        500: "d",
        1000: "m",
    }

    values = []
    number_str = str(number)
    for i in range(len(number_str)):
        char = number_str[i]
        if char == "4":
            values.append("c")
            values.append("i")
        elif char == "9":
            values.append("x")
            values.append("i")
        else:
            values.append(roman_values[int(char)])

    return "".join(values)

