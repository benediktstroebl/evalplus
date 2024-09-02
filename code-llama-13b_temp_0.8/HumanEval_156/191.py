
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

    def _create_number_to_roman_dict(
            numbers: tuple, romans: tuple
    ) -> dict:
        return {num: roman for num, roman in zip(numbers, romans)}

    number_to_roman = {
        'units': _create_number_to_roman_dict((1, 4, 5, 9, 10), ('i', 'iv', 'v', 'ix', 'x')),
        'tens': _create_number_to_roman_dict((1, 4, 5, 9, 10), ('x', 'xl', 'l', 'xc', 'c')),
        'hundreds': _create_number_to_roman_dict((1, 4, 5, 9, 10), ('c', 'cd', 'd', 'cm', 'm')),
    }

    number_string = str(number)
    len_number_string = len(number_string)
    if len_number_string < 4:
        return number_to_roman[f'{"units" * len_number_string}'][int(number_string)]

    number_string_digits = tuple(number_string)
    return (
        number_to_roman['hundreds'][int(number_string_digits[0])] +
        number_to_roman['tens'][int(number_string_digits[1])] +
        number_to_roman['units'][int(number_string_digits[2])]
    )

