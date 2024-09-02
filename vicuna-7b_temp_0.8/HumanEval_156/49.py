
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
        'I': 'i',
        'V': 'v',
        'X': 'x',
        'L': 'iv',
        'C': 'c',
        'D': 'd',
        'M': 'm',
        'N': 'n',
        'P': 'p',
        'R': 'r',
        'S': 's',
        'T': 't',
        'U': 'u',
        'F': 'f',
        'G': 'g',
        'H': 'h',
        'J': 'ij',
        'K': 'k',
        'Q': 'q',
        'R': 'r',
        'S': 's',
        'T': 't',
        'V': 'v',
        'X': 'x',
        'Z': 'z',
    }

    numeral = str(number)

    numeral_map = {
        '0': '',
        '1': 'i',
        '2': 'ii',
        '3': 'iii',
        '4': 'iv',
        '5': 'v',
        '6': 'vi',
        '7': 'vii',
        '8': 'viii',
        '9': 'ix',
    }

    numeral_list = numeral.split()
    roman_list = []

    for i, numeral in enumerate(numeral_list):
        roman = numeral_map[numeral] or numeral
        if i == 0:
            roman = roman_map[roman] or roman
        roman_list.append(roman)

    return ' '.join(roman_list)