from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    indices = [range(len(numbers)) for _ in range(len(numbers))]
    indices = [i[::-1] for i in indices]
    current_max = numbers[0]
    current_indices = [i for i in indices if numbers[i] > current_max]
    return [current_max] + [numbers[i] for i in current_indices]

