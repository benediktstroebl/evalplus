from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # How many numbers are there?
    n = len(numbers)

    # Get the first two smallest numbers
    min_val, min_idx = find_min(numbers)
    second_smallest_val, second_smallest_idx = find_min(numbers, excluded_idxs={min_idx})

    # If the smallest number is the closest to the next smallest number
    if abs(second_smallest_val - min_val) < abs(second_smallest_val - numbers[n - 1]):
        return (numbers[min_idx], numbers[second_smallest_idx])

    # If the smallest number is the closest to the last number
    elif abs(min_val - numbers[n - 1]) < abs(second_smallest_val - numbers[n - 1]):
        return (numbers[second_smallest_idx], numbers[n - 1])

    # If the last number is the closest to the next smallest number
    elif abs(numbers[n - 1] - min_val) < abs(numbers[n - 1] - second_smallest_val):
        return (numbers[n - 1], numbers[min_idx])

    return (numbers[second_smallest_idx], numbers[n - 1])

