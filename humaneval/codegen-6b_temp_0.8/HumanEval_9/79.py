from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    n = len(numbers)
    m = int(n / 2)

    rolling_max_arr = [numbers[0]] * m

    for i in range(n):
        if i < m:
            rolling_max_arr[i] = max(numbers[i], rolling_max_arr[i])
        else:
            rolling_max_arr[i] = max(numbers[i], rolling_max_arr[i - 1], rolling_max_arr[i - m])

    return rolling_max_arr

