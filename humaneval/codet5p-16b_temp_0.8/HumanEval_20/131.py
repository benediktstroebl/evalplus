from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    numbers.sort()

    start, end = 0, len(numbers) - 1
    diff = float('inf')

    while start < end:
        new_diff = abs(numbers[start] + numbers[end])
        if new_diff < diff:
            diff = new_diff
            closest_elements = (numbers[start], numbers[end])

        if numbers[start] + numbers[end] < 0:
            start += 1
        else:
            end -= 1
    return closest_elements
