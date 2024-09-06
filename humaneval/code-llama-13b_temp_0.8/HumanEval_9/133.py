from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # Time complexity: O(n)
    # Space complexity: O(n)
    stack: List[Tuple[int, int]] = []
    max_so_far = -float('inf')
    for i in numbers:
        if max_so_far < i:
            max_so_far = i
        while stack and stack[-1][0] < i:
            stack.pop()
        stack.append((i, max_so_far))
    return [stack[i][1] for i in range(len(numbers))]

