from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    closest_elements = []
    smallest_diff = numbers[1] - numbers[0]

    for index in range(1, len(numbers)):
        current_diff = numbers[index] - numbers[index - 1]
        if current_diff < smallest_diff:
            smallest_diff = current_diff
            closest_elements = [numbers[index - 1], numbers[index]]
        elif current_diff == smallest_diff:
            closest_elements.append(numbers[index - 1])
            closest_elements.append(numbers[index])

    return tuple(sorted(closest_elements))

