from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    max_index: List[int] = []
    max_value: int = numbers[0]
    for index in range(len(numbers)):
        if max_value < numbers[index]:
            max_value = numbers[index]
            max_index.append(index)
        else:
            max_value = max_value
    return max_index

