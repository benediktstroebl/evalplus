from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    min_distance = float('inf')
    min_index = -1

    for i, number in enumerate(numbers):
        if number == min_distance:
            continue
        elif number < min_distance:
            min_distance = number
            min_index = i
        else:
            if numbers[i] == min_distance:
                continue

    return numbers[min_index], numbers[min_index + 1]

