from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if len(numbers) <= 1:
        return numbers
    n = len(numbers)
    result = []
    for i in range(n):
        current_max = max(numbers[:i+1])
        result.append(current_max)
        numbers.pop(0)
        if len(numbers) == 0:
            break
    return result

