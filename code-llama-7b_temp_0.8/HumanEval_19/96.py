from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    if numbers == '':
        return ''
    num_list: List[str] = []
    while numbers != '':
        num_list.append(numbers[numbers.find(' ') + 1:numbers.find(' ', numbers.find(' ') + 2)])
        numbers = numbers[numbers.find(' ', numbers.find(' ', numbers.find(' ') + 2) + 1):]
    num_list.sort()
    result = num_list[0]
    for i in range(1, len(num_list)):
        result += ' ' + num_list[i]
    return result

