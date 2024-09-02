
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

    def solve_one_case(number):
        roman_numerals = [
            ('', 'I', 'V', 'X'),
            ('', 'X', 'L', 'C'),
            ('', 'C', 'D', 'M'),
            ('', 'M', '', ''),
        ]
        return roman_numerals[0][3] * (number // 1000) + \
            roman_numerals[1][3] * ((number % 1000) // 100) + \
            roman_numerals[2][3] * ((number % 100) // 10) + \
            roman_numerals[3][3] * (number % 10)
    
    output = ''
    while number:
        output += solve_one_case(number)
        number -= 1
    return output

