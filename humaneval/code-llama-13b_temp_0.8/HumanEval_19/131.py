from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    numbers_list = numbers.split()
    numberals_mapping = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
                         'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    for i in range(len(numbers_list)):
        numbers_list[i] = numberals_mapping[numbers_list[i]]
    numbers_list.sort()
    for i in range(len(numbers_list)):
        for key in numberals_mapping:
            if numberals_mapping[key] == numbers_list[i]:
                numbers_list[i] = key
                break
    return ' '.join(numbers_list)

