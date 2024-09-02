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
        raise ValueError("Expected at least 2 numbers")

    distance = 1e9
    indices = []
    for index, number in enumerate(numbers):
        distance_new = abs(number - (sum(numbers[:index]) / len(numbers[:index])))
        if distance_new < distance:
            distance = distance_new
            indices = [index]
        elif distance_new == distance:
            indices.append(index)

    return (numbers[indices[0]], numbers[indices[1]]
