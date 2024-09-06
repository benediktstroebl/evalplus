from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # TODO: Write an implementation
    min_gap = 100
    min_diff = 0
    min_number = 0
    number_1 = 0
    number_2 = 0

    for i, number in enumerate(numbers):
        for number_2 in numbers[i + 1:]:
            diff = abs(number - number_2)
            if diff < min_diff:
                min_diff = diff
                min_number = number
                number_1 = number
                number_2 = number_2
            if min_diff <= min_gap:
                min_gap = min_diff

    return number_1, number_2

