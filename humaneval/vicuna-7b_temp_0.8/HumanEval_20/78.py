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
        return None
    sorted_numbers = sorted(numbers)
    min_diff = float('inf')
    max_diff = 0.0
    min_index = 0
    max_index = len(numbers) - 1
    for i in range(1, len(numbers)):
        diff = float(numbers[i]) - float(numbers[min_index])
        min_diff = min(min_diff, diff)
        max_diff = max(max_diff, diff)
        if diff < 0.0:
            min_index += 1
        else:
            max_index -= 1
    return min_index, max_index

