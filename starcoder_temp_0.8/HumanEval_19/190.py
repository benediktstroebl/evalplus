from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    output: List[str] = []
    split_numbers: List[str] = numbers.split(" ")

    for num in sorted(split_numbers, key=lambda x: int(x)):
        output.append(num)

    return " ".join(output)

