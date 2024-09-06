from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # return [max(numbers[:i]) for i in range(len(numbers))]
    max_val = numbers[0]
    result = []

    for i in range(len(numbers)):
        max_val = max(numbers[i], max_val)
        result.append(max_val)

    return result

