from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    def char_to_num(char: str) -> int:
        if char in ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'):
            return int(char)
        else:
            raise Exception('Invalid input')

    def num_to_char(num: int) -> str:
        if num in range(10):
            return f'{num}'
        else:
            raise Exception('Invalid input')

    sorted_string = ''
    numbers_list = numbers.split()
    for i in range(len(numbers_list)):
        if numbers_list[i] != '':
            temp_num = char_to_num(numbers_list[i])
            sorted_string += num_to_char(temp_num) + ' '
    return sorted_string.rstrip()

