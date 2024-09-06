from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # This is a naive implementation
    # TODO: Optimize this function if necessary
    current_max = numbers[0]
    current_max_index = 0

    for num in numbers:
        if num > current_max:
            current_max = num
            current_max_index = 0
        else:
            current_max_index += 1

    return [current_max] + [current_max_index] * (len(numbers) - len(current_max))

