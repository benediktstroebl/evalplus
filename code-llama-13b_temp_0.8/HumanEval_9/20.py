from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    rolling_max_elements = [1] * len(numbers)
    for idx in range(len(numbers)):
        for idx2 in range(idx):
            if numbers[idx] <= numbers[idx2]:
                break
            else:
                rolling_max_elements[idx] = idx2 + 1
    return rolling_max_elements

