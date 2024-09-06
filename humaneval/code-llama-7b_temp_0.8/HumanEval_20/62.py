from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements.")

    min_diff = float("inf")
    min_diff_nums = None

    for i, el1 in enumerate(numbers):
        for j, el2 in enumerate(numbers):
            diff = abs(el1 - el2)
            if i != j and diff < min_diff:
                min_diff = diff
                min_diff_nums = (el1, el2)

    return min_diff_nums

