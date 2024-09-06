from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    if not numbers:
        return ''

    num_list = numbers.split()
    # check if input is valid
    if not all(num.isdigit() or num in ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'] for num in num_list):
        raise ValueError('Invalid numberals')

    # check if digits are in numberals
    num_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    num_list = [num if num.isdigit() else num_dict[num] for num in num_list]

    num_list = sorted(num_list, key=int)

    return ' '.join([str(i) for i in num_list])

