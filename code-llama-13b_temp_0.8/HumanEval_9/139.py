from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    rolling_max_numbers = [0] * len(numbers)
    stack = []
    for index, number in enumerate(numbers):
        while stack and numbers[stack[-1]] < number:
            stack.pop()
        if not stack:
            rolling_max_numbers[index] = number
        else:
            rolling_max_numbers[index] = numbers[stack[-1]]
        stack.append(index)
    return rolling_max_numbers

