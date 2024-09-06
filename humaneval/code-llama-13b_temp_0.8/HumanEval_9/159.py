from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # We need to keep at least 2 values at each moment: the current one, and the maximum one
    # so we cannot start from a size of 0
    stack = [(float("-inf"), float("-inf"))]

    output = []

    for n in numbers:
        while stack[-1][0] < n:
            stack.pop()
        max_value = stack[-1][1]

        stack.append((n, max_value))
        output.append(max_value)

    return output

