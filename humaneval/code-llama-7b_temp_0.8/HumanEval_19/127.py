from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Number to numberal
    ord_to_num = {0: 'zero',
                  1: 'one',
                  2: 'two',
                  3: 'three',
                  4: 'four',
                  5: 'five',
                  6: 'six',
                  7: 'seven',
                  8: 'eight',
                  9: 'nine'}
    # Numberal to number
    num_to_ord = {'zero': 0,
                  'one': 1,
                  'two': 2,
                  'three': 3,
                  'four': 4,
                  'five': 5,
                  'six': 6,
                  'seven': 7,
                  'eight': 8,
                  'nine': 9}

    numbers_list: List[int] = []

    for number in numbers.split():
        numbers_list.append(num_to_ord[number])

    numbers_list.sort()

    return ' '.join([ord_to_num[number] for number in numbers_list])

