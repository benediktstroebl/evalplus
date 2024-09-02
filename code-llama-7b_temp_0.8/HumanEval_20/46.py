from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    smallest_diff = float("inf")
    smallest_pair = None
    for i, num in enumerate(numbers[:-1]):
        for next_num in numbers[i + 1 :]:
            diff = abs(next_num - num)
            if diff < smallest_diff:
                smallest_diff = diff
                smallest_pair = (num, next_num)

    return smallest_pair

