
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
    roman_map = {
        'I': 'I', 'V': 'V', 'X': 'X', 'L': 'X',
        'C': 'IV', 'D': 'IV', 'M': 'I', 'N': 'I',
        'P': 'XL', 'R': 'XL', 'S': 'XL', 'T': 'XL',
        'G': 'XC', 'F': 'XC', 'B': 'XC', 'H': 'XC'
    }
    roman_num = str(number)
    for i in range(len(roman_num)):
        if roman_num[i] == '1':
            numeral = roman_map[roman_num[i+1]]
        elif roman_num[i] == '2':
            numeral = roman_map[roman_num[i+1]] + roman_map['C']
        elif roman_num[i] == '3':
            numeral = roman_map[roman_num[i+1]] + roman_map['CD']
        elif roman_num[i] == '4':
            numeral = roman_map[roman_num[i+1]] + roman_map['D']
        elif roman_num[i] == '5':
            numeral = roman_map[roman_num[i+1]] + roman_map['CM']
        elif roman_num[i] == '6':
            numeral = roman_map[roman_num[i+1]] + roman_map['D'] + roman_map['C']
        elif roman_num[i] == '7':
            numeral = roman_map[roman_num[i+1]] + roman_map['CM'] + roman_map['D']
        elif roman_num[i] == '8':
            numeral = roman_map[roman_num[i+1]] + roman_map['C'] + roman_map['CD'] + roman_map['D']
        elif roman_num[i] == '9':
            numeral = roman_map[roman_num[i+1]] + roman_map['XC']
        else
