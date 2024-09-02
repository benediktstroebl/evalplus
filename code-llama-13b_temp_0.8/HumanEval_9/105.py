from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if len(numbers) == 0:
        return numbers

    last_rolling_max = numbers[0]
    rolling_max_list = [last_rolling_max]

    for n in numbers[1:]:
        if n > last_rolling_max:
            last_rolling_max = n

        rolling_max_list.append(last_rolling_max)

    return rolling_max_list

