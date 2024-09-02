
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
    # Your code here
    roman = {}
    roman[1000] = 'M'
    roman[900] = 'CM'
    roman[500] = 'D'
    roman[400] = 'CD'
    roman[100] = 'C'
    roman[90] = 'XC'
    roman[50] = 'L'
    roman[40] = 'XL'
    roman[10] = 'X'
    roman[9] = 'IX'
    roman[5] = 'V'
    roman[4] = 'IV'
    roman[1] = 'I'
    roman[0] = ''
    roman_str = ""
    for i in range(1, 1001):
        if number == i:
            return roman_str
        if i <= number:
            roman_str += roman[i]
            number -= i
    return roman_str
