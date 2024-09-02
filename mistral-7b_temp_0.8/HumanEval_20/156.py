from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # SOLUTION

    assert len(numbers) >= 2

    closest_numbers = numbers[0], numbers[1]
    for number in numbers[2:]:
        distance_to_closest_numbers = abs(number - closest_numbers[0])
        if distance_to_closest_numbers < abs(number - closest_numbers[1]):
            closest_numbers = number, closest_numbers[1]
        elif distance_to_closest_numbers == abs(number - closest_numbers[1]):
            closest_numbers = min(number, closest_numbers[0]), max(number, closest_numbers[0])

    return closest_numbers

