from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    output: List[int] = []
    for i in range(len(numbers)):
        max_value = numbers[i]
        if i == 0:
            output.append(max_value)
            continue
        if numbers[i] > max_value:
            max_value = numbers[i]
        output.append(max_value)
    return output

