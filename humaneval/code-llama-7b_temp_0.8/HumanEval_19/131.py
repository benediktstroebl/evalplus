from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    numbers_list = numbers.split(' ')
    numbers_set = set(numbers_list)

    def get_order(element: str) -> int:
        """ Return a number to indicate the order of the input element """
        return int(element.split('o')[1]) if element != 'zero' else 0

    numbers_list.sort(key=get_order)
    numbers_list_str = ' '.join(numbers_list)
    return numbers_list_str

