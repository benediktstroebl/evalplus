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
        return -1

    # Find the minimum and maximum number in the list.
    min_val = min(numbers)
    max_val = max(numbers)

    # Iterate through all the numbers in the list and find the difference between each one and both the min and max.
    # If the difference is smaller than the current difference for the closest pair of numbers, update the closest
    # pair of numbers to the current pair.
    current_diff = max_val - min_val
    closest_pair = (min_val, max_val)
    for num in numbers:
        diff = abs(num - min_val)
        if diff < current_diff:
            closest_pair = (min_val, num)
            current_diff = diff
        diff = abs(num - max_val)
        if diff < current_diff:
            closest_pair = (num, max_val)
            current_diff = diff

    return closest_pair

