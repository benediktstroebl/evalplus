
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

    # Transform the number to a list of digits (e.g. 19 becomes [1,9])
    number_list = []
    while number > 0:
        digit = number % 10
        number_list.insert(0, digit)
        number = number // 10

    roman_list = []
    for index, num in enumerate(number_list):
        if num == 9:
            roman_list.append('ix')
        elif num == 4:
            roman_list.append('iv')
        elif num >= 5:
            if num % 5 == 0:
                roman_list.append('v' * (num // 5))
            else:
                roman_list.append('v' * (num // 5))
                roman_list.append('i' * (num % 5))
        else:
            roman_list.append('i' * num)

    return ''.join(roman_list)
