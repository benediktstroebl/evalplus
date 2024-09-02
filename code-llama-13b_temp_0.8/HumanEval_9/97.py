from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_number, max_index = numbers[0], 0
    rolling_max = []
    for index, number in enumerate(numbers):
        if max_number < number:
            max_number, max_index = number, index
        rolling_max.append(max_number)
    return [numbers[index] for index in range(len(numbers)) if index >= max_index]

