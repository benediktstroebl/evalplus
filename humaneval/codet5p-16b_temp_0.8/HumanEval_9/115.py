from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    result = []
    if len(numbers) == 0:
        return numbers
    max_value = numbers[0]
    result.append(max_value)
    for index, number in enumerate(numbers[1:]):
        if number > max_value:
            max_value = number
        else:
            max_value = max_value
        result.append(max_value)
    return result

