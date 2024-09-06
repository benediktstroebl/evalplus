from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    from collections import OrderedDict
    dictionary = OrderedDict()
    for i in range(10):
        dictionary[str(i)] = i
    dictionary['0'], dictionary['1'], dictionary['2'], dictionary['3'], dictionary['4'], dictionary['5'], dictionary[
        '6'], dictionary['7'], dictionary['8'], dictionary[
        '9'] = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    dictionary.move_to_end('0')
    dictionary.move_to_end('1')
    dictionary.move_to_end('2')
    dictionary.move_to_end('3')
    dictionary.move_to_end('4')
    dictionary.move_to_end('5')
    dictionary.move_to_end('6')
    dictionary.move_to_end('7')
    dictionary.move_to_end('8')
    dictionary.move_to_end('9')
    number_list = numbers.split(' ')
    new_list = []
    for number in number_list:
        new_list.append(dictionary[number])
    return ' '.join(str(x) for x in new_list)

