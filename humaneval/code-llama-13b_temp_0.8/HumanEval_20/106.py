from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    smallest_diff = numbers[1] - numbers[0]
    smallest_diff_pair = (numbers[0], numbers[1])

    for i, current_number in enumerate(numbers[:-1]):
        for j, other_number in enumerate(numbers[i + 1:]):
            current_diff = abs(current_number - other_number)

            if current_diff < smallest_diff:
                smallest_diff = current_diff
                smallest_diff_pair = (current_number, other_number)

    return smallest_diff_pair

