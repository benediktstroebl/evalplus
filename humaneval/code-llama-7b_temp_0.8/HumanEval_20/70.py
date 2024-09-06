from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    best_diff = float("inf")
    best_pair = None

    for i, first_num in enumerate(numbers):
        for second_num in numbers[i + 1 :]:
            diff = abs(first_num - second_num)
            if diff < best_diff:
                best_diff = diff
                best_pair = (first_num, second_num)

    return best_pair

