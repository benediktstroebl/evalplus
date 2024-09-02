from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    # Using the built-in functions min() and max() to find the two closest numbers
    min_value = min(numbers)
    max_value = max(numbers)

    if numbers.count(min_value) > 1:
        return min_value, numbers[numbers.index(min_value) + 1]
    elif numbers.count(max_value) > 1:
        return max_value, numbers[numbers.index(max_value) - 1]
    else:
        return min_value, max_value

