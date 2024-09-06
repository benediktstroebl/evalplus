from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    def sort(numbers: List[str]) -> List[str]:
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if numbers[j] < numbers[i]:
                    numbers[i], numbers[j] = numbers[j], numbers[i]
        return numbers
    numbers = numbers.split(' ')
    return''.join(sort(numbers))
