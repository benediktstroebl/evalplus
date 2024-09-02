from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    # Closest 2 elements' indices
    # Distance between those elements
    closest_pair_indices = 0, 1
    closest_distance = abs(numbers[0] - numbers[1])

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            distance = abs(numbers[i] - numbers[j])
            if distance < closest_distance:
                closest_pair_indices = i, j
                closest_distance = distance

    return numbers[closest_pair_indices[0]], numbers[closest_pair_indices[1]]

