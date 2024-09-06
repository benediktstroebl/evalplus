from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    output = []
    stack = []

    for i, num in enumerate(numbers):
        while stack and stack[-1] <= num:
            stack.pop()
        stack.append(num)
        output.append(stack[-1])

    return output

