
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

    if number < 1 or number > 1000:
        raise ValueError("Number is not within range of 1-1000")

    roman_dict = {1: "i", 5: "v", 10: "x", 50: "l", 100: "c", 500: "d", 1000: "m"}
    output = []
    number_list = [int(x) for x in str(number)]

    for digit in number_list:
        if digit == 4 or digit == 9:
            output.append(roman_dict[digit * 10])
        elif digit == 5 or digit == 0:
            output.append(roman_dict[digit * 5])
        elif digit <= 3:
            output.append(roman_dict[digit])
        else:
            output.append(roman_dict[digit * 10])

    output = "".join(output)
    output = output.replace("iv", "i")
    output = output.replace("ix", "i")
    output = output.replace("xl", "x")
    output = output.replace("xc", "x")
    output = output.replace("cd", "c")
    output = output.replace("cm", "c")

    return output

