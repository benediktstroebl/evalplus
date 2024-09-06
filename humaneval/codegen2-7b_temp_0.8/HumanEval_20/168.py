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
        raise ValueError(f"{numbers} must have at least two elements")
    min_index = 0
    max_index = 1
    current_min = numbers[min_index]
    for index in range(1, len(numbers)):
        current_number = numbers[index]
        if abs(current_number - current_min) < abs(current_number - numbers[max_index]):
            min_index = index
            current_min = current_number
        else:
            max_index = index
    return (min_index, max_index)
