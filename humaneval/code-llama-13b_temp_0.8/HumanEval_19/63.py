from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # define a dictionary of numberals
    number_dict = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    # split the input string into a list
    numbers_list = numbers.split(' ')
    # create a new list to hold the integers from the numberal dictionary
    new_list: List[int] = []
    # iterate through the list of numberals and find the corresponding integer in the numberal dictionary
    for number in numbers_list:
        new_list.append(number_dict[number])
    # sort the new list and convert it back into a string
    return ' '.join([str(num) for num in sorted(new_list)])

