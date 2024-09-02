from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        return []
    max_val = numbers[0]
    rolling_max_list = [max_val]
    current = [max_val]
    for i in range(1, len(numbers)):
        if numbers[i] > max_val:
            max_val = numbers[i]
            rolling_max_list = current[:]
            current = [max_val]
        else:
            current.append(max_val)
    return rolling_max_list + current

