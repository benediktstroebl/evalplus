
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
    roman_numerals = {
        'I': 'i', 'V': 'v', 'X': 'x', 'L': 'l', 'C': 'c', 'D': 'd',
        'M': 'm', 'N': 'n', 'P': 'p', 'R': 'r', 'S': 's', 'T': 't',
        'U': 'u', 'F': 'f', 'G': 'g', 'H': 'h', 'J': 'j', 'K': 'k',
        'Q': 'q', 'X': 'x', 'Z': 'z', 'H': 'h', 'G': 'g', 'F': 'f',
        'E': 'e', 'D': 'd', 'C': 'c', 'B': 'b', 'A': 'a', 'I': 'i',
        'V': 'v', 'U': 'u', 'T': 't', 'S': 's', 'R': 'r', 'P': 'p',
        'N': 'n', 'M': 'm', 'L': 'l', 'K': 'k', 'J': 'j', 'X': 'x',
        'Y': 'y', 'H': 'h', 'V': 'v', 'F': 'f', 'D': 'd', 'R': 'r',
        'Q': 'q', 'U': 'u', 'Z': 'z'
    }

    number_digits = str(number)

    roman_numerals_list = number_digits.split()
    roman_numerals_list.reverse()

    result = ''

    for i in range(len(roman_numerals_list)):
        result = roman_numerals[roman_numerals_list[i]] + result

    return result.lower()