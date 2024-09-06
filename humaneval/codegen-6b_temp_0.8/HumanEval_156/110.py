
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
    # How to define an array of character to be returned?
    # char_list = []
    # for num in range(1,1000):
    #     char_list.append(num)
    #
    # Roman_char_list = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
    #
    # for Roman_num in Roman_char_list:
    #     if Roman_num < number:
    #         number -= Roman_num
    #         char_list.insert(0, Roman_char_list[Roman_num])
    #
    # return ''.join(char_list)

    # better solution
    arr = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    roman = ''
    i = 0
    while number > 0:
        while number >= val[i]:
            number -= val[i]
            roman += arr[i]
        i += 1

    return roman


