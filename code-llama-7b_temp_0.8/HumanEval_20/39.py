from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # Smallest distance
    closest_distance = numbers[1] - numbers[0]
    # Indices
    closest_indices = (0, 1)

    for i in range(2, len(numbers)):
        distance = numbers[i] - numbers[i - 1]
        if distance < closest_distance:
            closest_distance = distance
            closest_indices = (i - 1, i)

    return numbers[closest_indices[0]], numbers[closest_indices[1]]

