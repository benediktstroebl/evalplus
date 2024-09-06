from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        return []

    max_element_so_far: int = numbers[0]
    rolling_max_elements: List[int] = [numbers[0]]

    for i in range(1, len(numbers)):
        if numbers[i] > max_element_so_far:
            max_element_so_far = numbers[i]

        rolling_max_elements.append(max_element_so_far)

    return rolling_max_elements

