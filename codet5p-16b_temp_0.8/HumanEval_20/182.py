from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    min_elem_1 = numbers[0]
    min_elem_2 = numbers[0]
    max_elem_1 = numbers[0]
    max_elem_2 = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] < min_elem_1:
            min_elem_2 = min_elem_1
            min_elem_1 = numbers[i]
        elif numbers[i] < min_elem_2:
            min_elem_2 = numbers[i]
        if numbers[i] > max_elem_1:
            max_elem_2 = max_elem_1
            max_elem_1 = numbers[i]
        elif numbers[i] > max_elem_2:
            max_elem_2 = numbers[i]
    return (min_elem_1, max_elem_1) if min_elem_1 < max_elem_1 else (min_elem_2, max_elem_
