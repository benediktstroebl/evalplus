from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    if len(numbers) == 0:
        return ""
    if len(numbers) == 1:
        return numbers
    if len(numbers) == 2:
        if numbers.split()[0] < numbers.split()[1]:
            return numbers.split()[0] + " " + numbers.split()[1]
        else:
            return numbers.split()[1] + " " + numbers.split()[0]
    sorted_numbers: List[str] = sorted(numbers.split())
    for index, item in enumerate(sorted_numbers):
        if index == 0:
            pass
        elif sorted_numbers[index] < sorted_numbers[index - 1]:
            sorted_numbers[index] = sorted_numbers[index - 1] + " " + sorted_numbers[index]
        else:
            pass
    return " ".join(sorted_numbers)

