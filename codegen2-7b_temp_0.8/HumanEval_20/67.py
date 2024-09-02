from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    if len(numbers) < 2:
        raise ValueError("Incorrect number of numbers supplied for this function")

    min_index = 0
    min_value = numbers[0]

    for i in range(1, len(numbers)):
        value = numbers[i]
        if abs(min_value) > abs(value):
            min_value = value
            min_index = i

    return (numbers[min_index], min_value
