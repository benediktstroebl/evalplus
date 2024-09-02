
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

    ints_to_roman = {1:'i', 5:'v', 10:'x', 50:'l', 100:'c', 500:'d', 1000:'m'}

    # we get an ordered list of values that need to be transformed to roman
    # notation, for example: 19 would be [1000, 100, 10, 1]
    roman_numbers = [int(i) for i in str(number)]
    roman_numbers.reverse()

    output_string = ''

    for i in roman_numbers:
        # if our number is 1000, 100, etc.
        if i > 0:
            # iterate over our dictionary and return the roman numeral
            # for our current number
            for k, v in ints_to_roman.items():
                if i >= k:
                    num_to_repeat = int(i / k)
                    roman_numeral = v * num_to_repeat
                    output_string += roman_numeral

    return output_string



