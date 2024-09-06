
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
    num_dict = {1:"i", 5:"v", 10:"x", 50:"l", 100:"c", 500:"d", 1000:"m"}
    return_roman = ''
    num_string = str(number)
    for i in range(len(num_string)):
        if i == 0:
            return_roman = num_dict[int(num_string[i])]
        elif int(num_string[i]) <= 3:
            return_roman += num_dict[int(num_string[i])]*(5-int(num_string[i-1]))
        elif int(num_string[i]) <= 5:
            return_roman += num_dict[int(num_string[i-1])]
            return_roman += num_dict[int(num_string[i])]
        elif int(num_string[i]) <= 8:
            return_roman += num_dict[int(num_string[i])-2]
            return_roman += num_dict[int(num_string[i-1])]
        elif int(num_string[i]) <= 10:
            return_roman += num_dict[int(num_string[i])]
    return return_roman


