from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_list = [None] * 10
    max_so_far = None

    for i in range(1, len(numbers) + 1):
        if max_so_far is None or numbers[i - 1] > max_so_far:
            max_list[i - 1] = max(max_list[i - 1], numbers[i - 1])
        else:
            max_list[i - 1] = max_list[i - 2]

        if numbers[i] > max_so_far:
            max_so_far = numbers[i]

    return max_list[-1]

