from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    output_list: List[int] = [0] * len(numbers)
    for index, _ in enumerate(numbers):
        if index == 0:
            output_list[index] = numbers[index]
        else:
            output_list[index] = max(numbers[index], numbers[index] + output_list[index - 1])
    return output_list

