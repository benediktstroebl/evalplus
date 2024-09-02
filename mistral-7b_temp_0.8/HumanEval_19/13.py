from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # NOTE: You may use the following code as a starting point, but you are not required to keep it
    # numbers_to_ints = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6,
    #                    'seven': 7, 'eight': 8, 'nine': 9}
    # numbers_to_strs = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five',
    #                    '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}
    # sorted_numbers = []
    # for number in numbers.split():
    #     int_number = numbers_to_ints[number]
    #     sorted_numbers.append(number)
    # sorted_numbers.sort()
    # return ' '.join(sorted_numbers)

    # sorting the numbers
