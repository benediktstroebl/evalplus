from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    rolling_max_until_index = []
    for index, number in enumerate(numbers):
        if not rolling_max_until_index:
            rolling_max_until_index.append(number)
        else:
            last_rolling_max = rolling_max_until_index[-1]
            if last_rolling_max <= number:
                rolling_max_until_index.append(number)
            else:
                rolling_max_until_index.append(last_rolling_max)
    return rolling_max_until_index

