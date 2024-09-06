from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_value = numbers[0]
    for index, current_element in enumerate(numbers[1:]):
        if current_element > max_value:
            max_value = current_element
        numbers[index + 1] = max_value

    return numbers

