from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    if not numbers:
        raise ValueError("At least one number is required.")
    if len(numbers) < 2:
        raise ValueError("At least two numbers are required.")

    min_diff = float('inf')
    closest_pair = (0, 0)

    for i in range(1, len(numbers)):
        for j in range(i):
            diff = numbers[i] - numbers[j]
            if diff < min_diff:
                min_diff = diff
                closest_pair = (i, j)

    return closest_pair[0], closest_pair[1]