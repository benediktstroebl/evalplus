from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    sorted_numbers = sorted(list(numbers))
    min_distance = float("inf")
    closest_numbers = sorted_numbers[0], sorted_numbers[1]

    for i, first_number in enumerate(sorted_numbers[:-1]):
        for second_number in sorted_numbers[i + 1:]:
            if abs(first_number - second_number) < min_distance:
                closest_numbers = first_number, second_number
                min_distance = abs(first_number - second_number)

    return closest_numbers

