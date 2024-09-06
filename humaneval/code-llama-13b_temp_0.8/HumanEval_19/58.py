from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    if len(numbers.split()) == 1:
        return numbers

    numbers = numbers.split()

    def convert_to_number(number: str) -> int:
        return {
            'zero': 0,
            'one': 1,
            'two': 2,
            'three': 3,
            'four': 4,
            'five': 5,
            'six': 6,
            'seven': 7,
            'eight': 8,
            'nine': 9,
        }[number]

    def compare(a: str, b: str) -> int:
        return convert_to_number(a) - convert_to_number(b)

    return ' '.join(sorted(numbers, key=cmp_to_key(compare)))

