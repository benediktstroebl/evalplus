from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    n = 5  # maximum number of elements to consider
    current_max = numbers[0]
    current_index = 0

    for i in range(n):
        if numbers[i] > current_max:
            current_max = numbers[i]
        elif numbers[i] == current_max:
            current_index += 1
            if current_index == n:
                yield current_max
                current_index = 0
                current_max = numbers[i]

    if current_index != 0:
        yield current_max