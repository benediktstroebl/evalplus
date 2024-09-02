from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    result = []
    for i in range(len(numbers)):
        max_element = numbers[i]
        for j in range(i, len(numbers)):
            if numbers[j] > max_element:
                max_element = numbers[j]
        result.append(max_element)

    return result

