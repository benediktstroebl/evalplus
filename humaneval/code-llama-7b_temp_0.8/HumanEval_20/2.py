from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    smallest_distance = None
    largest_distance = None
    for i in range(len(numbers) - 1):
        current_distance = abs(numbers[i] - numbers[i + 1])
        if smallest_distance is None and largest_distance is None:
            smallest_distance = current_distance
            largest_distance = current_distance
            continue
        if current_distance > largest_distance:
            largest_distance = current_distance
        elif current_distance < smallest_distance:
            smallest_distance = current_distance

    return (
        min(numbers, key=lambda x: abs(x - numbers[numbers.index(min(numbers))])),
        max(numbers, key=lambda x: abs(x - numbers[numbers.index(max(numbers))])),
    )

