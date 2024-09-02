from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    min_diff = float('inf')
    min_diff_index = -1
    min_diff_number = None
    min_diff_other_number = None

    for i in range(len(numbers) - 1):
        if numbers[i] == numbers[i + 1]:
            continue

        diff = float(numbers[i]) - float(numbers[i + 1])
        if diff < min_diff:
            min_diff, min_diff_index = diff, i
            min_diff_number, min_diff_other_number = numbers[i], numbers[i + 1]
        elif diff == min_diff and numbers[i] < numbers[i + 1]:
            min_diff, min_diff_index = diff, i
            min_diff_number, min_diff_other_number = numbers[i], numbers[i + 1]
    return min_diff_number, min_diff_other_number

