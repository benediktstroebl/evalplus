from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if len(numbers) == 0:
        return []
    max_element = numbers[0]
    for i in range(1, len(numbers)):
        if max_element < numbers[i]:
            max_element = numbers[i]
        else:
            max_element = max(max_element, numbers[i])
    return [max_element] + rolling_max(numbers[1:
