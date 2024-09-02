from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    #
    # 3-step rolling max
    #
    max_3_roll = []
    current_max = None
    for number in numbers:
        if current_max is None:
            current_max = number
            continue
        elif number > current_max:
            max_3_roll.append(current_max)
            current_max = number
        else:
            max_3_roll.append(current_max)
            current_max = number
    max_3_roll.append(current_max)
    return max_3_roll

