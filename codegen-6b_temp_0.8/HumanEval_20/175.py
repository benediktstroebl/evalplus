from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    min_diff = min(numbers[0] - numbers[1], numbers[-1] - numbers[-2])
    for i in range(1, len(numbers)):
        num_diff = numbers[i] - numbers[i - 1]
        # We want to find pairs of elements that are closest to each other.
        # So we will use the min_diff to store our previous closest pair.
        if num_diff < min_diff:
            min_diff = num_diff
            # if the new pairs are closer to each other, then we will store the new pair as the closest
            min_pair = (numbers[i - 1], numbers[i])
    return min_pair

