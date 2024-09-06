from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        return []

    stack = [0]
    max_list = [numbers[0]]

    for i in range(1, len(numbers)):
        if numbers[i] >= numbers[stack[-1]]:
            stack.append(i)

        if numbers[stack[-1]] <= numbers[i]:
            stack.pop()

        max_list.append(numbers[stack[-1]])

    return max_list

