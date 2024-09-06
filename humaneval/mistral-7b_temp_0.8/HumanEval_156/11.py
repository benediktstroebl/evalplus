
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

    roman_alphabet = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
    roman_numeral = [1000, 500, 100, 50, 10, 5, 1]
    roman_number_list = []
    while number > 0:
        for index, roman in enumerate(roman_alphabet):
            if roman_numeral[index] > number:
                continue
            else:
                roman_number_list.append(roman)
                number -= roman_numeral[index]
                break

    for index, roman in enumerate(roman_alphabet):
        if roman_numeral[index] == number:
            roman_number_list.append(roman)
            break

    roman_number_list.reverse()

    return ''.join(roman_number_list)
