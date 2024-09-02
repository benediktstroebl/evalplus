
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
    # making a dictionary of roman numerals, value:key
    roman_dict = {1000 : 'm', 900 : 'cm', 500 : 'd', 400 : 'cd', 100 : 'c', 90 : 'xc', 50 : 'l', 40 : 'xl', 10 : 'x', 9 : 'ix', 5 : 'v', 4 : 'iv', 1 : 'i'}
    # converting the number to a string
    number = str(number)
    # making the string to a list
    num_list = list(number)
    # creating an empty string for the result
    result = ""

    # looping through the numbers in the list
    for num in num_list:
        # if the num is 1 or 2
        if num == '1' or num == '2':
            # the result is the value of the number times the key
            result += roman_dict[int(num) * int(num)]
        else:
            # otherwise just adding the key to the result
            result += roman_dict[int(num)]
    # returning the result
    return result
