
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
        raise ValueError("int_to_mini_roman only works with positive integer values")

    roman_dict = {1: "i", 5: "v", 10: "x"}
    roman_list = []
    while number!= 0:
        for value, roman in roman_dict.items():
            if number >= value:
                roman_list.append(roman)
                number -= value
                break
    return "".join(roman_list).lower
