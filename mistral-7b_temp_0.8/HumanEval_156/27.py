
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

    roman_numbers = {1: 'i', 5: 'v', 10: 'x', 50: 'l', 100: 'c', 500: 'd', 1000: 'm'}

    num = str(number)
    roman_number = ""
    count = 0

    for number in num:
        count += 1

        if count == 1:
            roman_number += roman_numbers.get(int(number))
        elif int(number) > int(num[count - 2]):
            roman_number += roman_numbers.get(int(number))
        elif int(number) < int(num[count - 2]):
            roman_number += roman_numbers.get(int(number)) + roman_numbers.get(int(num[count - 2]))
        else:
            roman_number += roman_numbers.get(int(number)) * int(num[count - 2])

    return roman_number

