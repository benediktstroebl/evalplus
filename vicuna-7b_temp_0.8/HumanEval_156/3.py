
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
        'I': '1', 'V': '5', 'X': '10', 'L': '50', 'C': '100', 'D': '500',
        'M': '1000'
    }
    number_alphabet = ''.join(sorted(map(str, number)))
    roman_alphabet = []
    for i in range(len(number_alphabet)):
        numeral = number_alphabet[i]
        index = numeral.find('A')
        if index != -1:
            roman_alphabet.append(numeral[:index])
            roman_alphabet.append(numeral[index+1:])
        else:
            roman_alphabet.append(numeral)
    roman_alphabet = ''.join(roman_alphabet)
    roman_alphabet = roman_map[roman_alphabet]
    return roman_alphabet.lower()