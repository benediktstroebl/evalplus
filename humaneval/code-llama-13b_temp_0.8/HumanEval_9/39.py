from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    rolling_max_ = [0] * len(numbers)
    stack: List[Tuple[int, int]] = []
    for index, number in enumerate(numbers):
        while stack and stack[-1][1] < number:
            stack.pop()
        rolling_max_[index] = stack[-1][0] if stack else number
        stack.append((number, number))
    return rolling_max_
