from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    n = len(numbers)
    if n < 2:
        return None, None
    elif n == 2:
        return numbers[0], numbers[1]
    smaller = min(numbers)
    smaller_index = numbers.index(smaller)
    larger = max(numbers)
    larger_index = numbers.index(larger)
    if abs(smaller - larger) < abs(smaller - numbers[smaller_index]):
        return smaller, larger
    else:
        return larger, smaller

