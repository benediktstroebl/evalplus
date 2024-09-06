from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    stack: List[Tuple[int, int]] = []
    res: List[int] = []

    for idx, num in enumerate(numbers):
        if stack and stack[-1][0] < num:
            stack.pop()

        stack.append((num, idx))
        res.append(stack[0][0])
    return res

