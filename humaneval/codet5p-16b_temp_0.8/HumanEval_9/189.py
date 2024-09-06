from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    last_index = len(numbers) - 1
    result = []

    for index in range(last_index + 1):
        max_so_far = numbers[index]
        for next_index in range(index, last_index + 1):
            if numbers[next_index] > max_so_far:
                max_so_far = numbers[next_index]
        result.append(max_so_far)

    return result

