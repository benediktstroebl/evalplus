from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    h = 2  # Hint, it's a simple case of binary search.
    # TODO: Examine the following while loop.  It will depend on your algorithm.
    while h > 0:
        if len(numbers) < h:
            h = h // 2
        else:
            half = int(len(numbers) / h)
            mid = half * h
            first = numbers[mid - h]
            second = numbers[mid + h]
            if abs(first - second) < abs(second - first):
                numbers = numbers[mid - h:mid + h + 1]
            else:
                numbers = numbers[mid - h + 1:mid + h + 1]
    return min(numbers), max(numbers)

