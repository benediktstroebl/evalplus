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
        raise ValueError("Need at least two numbers to find the closest")
    sorted_numbers = sorted(numbers)
    differences = []
    for i in range(1, len(sorted_numbers)):
        differences.append(abs(sorted_numbers[i] - sorted_numbers[i - 1]))
    min_diff = min(differences)
    min_diff_index = differences.index(min_diff)
    closest_numbers = (sorted_numbers[min_diff_index], sorted_numbers[min_diff_index - 1])
    return closest_numbers

