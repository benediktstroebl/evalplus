
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
    roman = ''
    dict_key = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
    dict_val = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # Starting from the smallest number, obtain its roman numeral equivalent.
    # Then, 'add' the key and value to the roman string, until we reach the
    # desired number.
    while number > 0:
        smallest = dict_val.index(min(dict_val))
        roman += dict_key[smallest]
        number -= dict_val[smallest]
        dict_val = dict_val[:smallest] + dict_val[smallest + 1:]
    return roman

