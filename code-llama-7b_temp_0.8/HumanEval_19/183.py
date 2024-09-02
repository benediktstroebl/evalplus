from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # convert input string to list
    number_list = numbers.split(" ")
    number_list = convert_number_list(number_list)
    number_list.sort()
    output = ""
    for i in range(len(number_list)):
        output = output + str(number_list[i]) + " "
    return output[:-1]

