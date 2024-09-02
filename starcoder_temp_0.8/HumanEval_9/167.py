from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # We start the rolling maximum from a dummy list of 1, because the first element is the biggest
    # element we can expect to have, until the given moment.
    rolling_max_list: List[int] = [1]
    for i in range(len(numbers)):
        rolling_max_list.append(max(numbers[i], rolling_max_list[i]))
    return rolling_max_list

