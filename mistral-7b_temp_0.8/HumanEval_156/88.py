
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

    ## TODO:
    ## Your code here
    roman_nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_letters = ['I', 'V', 'X', 'L', 'C', 'D', 'M']

    num_str = str(number)
    if len(num_str) == 1:
        if num_str[0] == '0':
            return 'I'
        else:
            return roman_nums[num_str[0]]
    elif len(num_str) == 2:
        if num_str[0] == '1' and num_str[1] == '0':
            return roman_letters[roman_letters.index(num_str[0])] + roman_letters[roman_letters.index(num_str[0])]
        elif num_str[0] == '9':
            return roman
