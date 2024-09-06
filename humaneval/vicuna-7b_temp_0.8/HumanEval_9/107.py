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
    max_ind = 0
    max_vals = [max_val]
    for num in numbers[1:]:
        if num > max_val:
            max_val = num
            max_ind = 1
        else:
            max_ind += 1
            max_vals.append(max_vals[-1])
    return max_vals[:max_ind]

