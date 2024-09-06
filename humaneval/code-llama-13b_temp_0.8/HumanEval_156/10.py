
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
    # local variables
    roman_list = []
    # mapping integer to roman numeral
    int_to_roman_dict = {
        1: "I",
        5: "V",
        10: "X",
        50: "L",
        100: "C",
        500: "D",
        1000: "M",
    }
    # mapping roman numeral to integer
    roman_to_int_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    for roman, integer in int_to_roman_dict.items():
        # check for digits that are in multiples of 1000
        if number >= 1000:
            num_of_digits = number // 1000  # number of digits
            roman_list.append(roman * num_of_digits)
            number -= num_of_digits * 1000
        # check for digits that are in multiples of 100
        if number >= 100:
            num_of_digits = number // 100  # number of digits
            roman_list.append(roman * num_of_digits)
            number -= num_of_digits * 100
        # check for digits that are in multiples of 10
        if number >= 10:
            num_of_digits = number // 10  # number of digits
            roman_list.append(roman * num_of_digits)
            number -= num_of_digits * 10
        # check for digits that are NOT in multiples of 10
        if number > 0:
            for roman, integer in int_to_roman_dict.items():
                if number == integer:
                    roman_list.append(roman)
        # check for digits that are in multiples of 5
