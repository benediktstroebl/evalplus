from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    result = []
    if numbers:
        result.append(numbers[0])
        max_element = numbers[0]

        for current in numbers[1:]:
            max_element = max(current, max_element)
            result.append(max_element)

    return result

