from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_index = 0
    max_value = numbers[0]
    curr_max_value = max_value
    curr_max_index = len(numbers) - 1

    for index in range(1, len(numbers)):
        if numbers[index] > curr_max_value:
            max_index = index
            curr_max_value = numbers[index]
            curr_max_index = curr_max_index - 1

        numbers[max_index] = curr_max_value

    return numbers[:max_index+1]

