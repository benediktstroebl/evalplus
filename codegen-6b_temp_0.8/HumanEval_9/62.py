from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    n = len(numbers)
    if n == 0:
        return []
    elif n == 1:
        return [numbers[0]]
    elif n == 2:
        return [max(numbers[0], numbers[1])]

    max_elem = numbers[0]
    rolling_max_elem = numbers[0]
    for i in range(1, n):
        new_elem = max(numbers[i], rolling_max_elem + numbers[i])
        rolling_max_elem = new_elem
        max_elem = max(max_elem, rolling_max_elem)

    return [max_elem] + rolling_max(numbers[1:])

