from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    numbers = numbers.split(' ')
    new_nums = []
    for num in numbers:
        num = int(num)
        new_nums.append(num)
    new_nums.sort()
    return_str = ''
    for num in new_nums:
        if str(num) == '0':
            return_str += 'zero '
        elif str(num) == '1':
            return_str += 'one '
        elif str(num) == '2':
            return_str += 'two '
        elif str(num) == '3':
            return_str += 'three '
        elif str(num) == '4':
            return_str += 'four '
        elif str(num) == '5':
            return_str += 'five '
        elif str(num) == '6':
            return_str +='six '
        elif str(num) == '7':
            return_str +='seven '
        elif str(num) == '8':
            return_str += '
