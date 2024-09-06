from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # numbers = list(numbers.split(' '))  # 28 ms
    numbers = numbers.split(' ')  # 20 ms
    numbers_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    numbers_int: List[int] = []
    for number in numbers:
        numbers_int.append(numbers_dict[number])
    numbers_int.sort()
    for i in range(len(numbers_int)):
        for number, value in numbers_dict.items():
            if value == numbers_int[i]:
                numbers[i] = number
    return ' '.join(numbers)

