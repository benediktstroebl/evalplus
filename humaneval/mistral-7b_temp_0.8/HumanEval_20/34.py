from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    def _get_closest_pair(numbers: List[float]) -> Tuple[float, float]:
        """Return a tuple of the closest pair of numbers in a list of numbers. The pair must be ordered smallest to largest.
        >>> _get_closest_pair([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
        (2.0, 2.2)
        >>> _get_closest_pair([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
        (2.0, 2.0)
        """
        if len(numbers) < 2:
            raise ValueError("list must have at least 2 elements")
        numbers.sort()
        return numbers[0], numbers[-1]

    closest_pair = _get_closest_pair(numbers)
    return closest_pair

