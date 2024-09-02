from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    current_max = max(numbers)
    last_index = 0
    for i in range(len(numbers) - 1):
        last_index += 1
        if numbers[last_index] > current_max:
            current_max = numbers[last_index]
        elif numbers[last_index] == current_max:
            current_max = max(current_max, numbers[last_index + 1])
        else:
            break
    return [current_max]

