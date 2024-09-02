from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if numbers == []:
        return []
    max_so_far = numbers[0]
    max_at_index = [max_so_far]
    for index in range(1, len(numbers)):
        if numbers[index] > max_so_far:
            max_so_far = numbers[index]
        max_at_index.append(max_so_far)
    return max_at_index
