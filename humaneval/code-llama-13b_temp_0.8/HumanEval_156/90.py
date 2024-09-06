
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
    # TODO: make this function work with other bases besides 10
    assert 1 <= number <= 1000

    def num_to_string(number, ones_char, tens_char, hundreds_char):
        ones_string = ones_char * (number % 10)
        tens_string = tens_char * ((number % 100) // 10)
        hundreds_string = hundreds_char * (number // 100)
        return hundreds_string + tens_string + ones_string

    roman_digits = 'ivxlcdm'

    roman_num = num_to_string(number, *roman_digits[:4])
    number //= 1000
    roman_num += num_to_string(number, *roman_digits[4:9])
    number //= 1000
    roman_num += num_to_string(number, *roman_digits[9:])

    return roman_num

