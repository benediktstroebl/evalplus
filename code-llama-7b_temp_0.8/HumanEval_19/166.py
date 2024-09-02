from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # errors
    numbers_list: List[str] = [number.strip() for number in numbers.split()]
    for number in numbers_list:
        if number not in ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']:
            raise ValueError(f"{number} is not a valid number.")

    # if input is an empty string, return an empty string
    if numbers == '':
        return ''

    # define helper functions
    def get_number(number: str) -> int:
        return {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
                'nine': 9}[number]

    def get_len(number: str) -> int:
        return len(number)

    # sort
    numbers_list.sort(key=lambda number: get_number(number))

    # return sorted string
    return ' '.join(numbers_list)

