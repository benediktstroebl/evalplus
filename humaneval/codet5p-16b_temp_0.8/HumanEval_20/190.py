from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    len_numbers = len(numbers)
    if len_numbers < 2:
        raise ValueError("Supplied list must have at least two elements.")
    min_diff = float('inf')
    smaller = None
    larger = None
    for i in range(len_numbers):
        for j in range(i + 1, len_numbers):
            if numbers[i] == numbers[j]:
                continue
            diff = numbers[j] - numbers[i]
            if diff < min_diff:
                min_diff = diff
                smaller = numbers[i]
                larger = numbers[j]
    return (smaller, larger)
