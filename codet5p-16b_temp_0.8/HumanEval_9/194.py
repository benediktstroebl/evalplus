from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    rolling_max: List[int] = []
    for idx, num in enumerate(numbers):
        rolling_max.append(num)
        for i in range(idx):
            if numbers[i] < num:
                rolling_max[idx] = num
                break
    return rolling_max

