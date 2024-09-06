from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_val = max(numbers)
    max_index = numbers.index(max_val)
    index = max_index
    result = [max_val]

    for i in range(1, len(numbers)):
        max_val = numbers[i]
        max_index = numbers.index(max_val)
        if max_index == index + 1:
            index = max_index
            result.append(max_val)
        else:
            index = max_index
            result.append(max_val)

    return result

