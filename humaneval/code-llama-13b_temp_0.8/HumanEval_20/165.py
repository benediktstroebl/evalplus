from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    assert len(numbers) >= 2, "The list must contain at least 2 numbers"
    closest_numbers = numbers[0], numbers[1]
    distance = abs(closest_numbers[0] - closest_numbers[1])
    for i in range(len(numbers) - 1):
        num_1 = numbers[i]
        num_2 = numbers[i + 1]
        new_distance = abs(num_1 - num_2)
        if new_distance < distance:
            closest_numbers = num_1, num_2
            distance = new_distance
    return closest_numbers

