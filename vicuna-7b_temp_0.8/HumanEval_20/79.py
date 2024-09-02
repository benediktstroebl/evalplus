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
    for i in range(len(numbers) - 1):
        min_diff = numbers[i] + numbers[i + 1]
        min_diff_index = i
        for j in range(i + 1, len(numbers)):
            if min_diff_index == i:
                min_diff = min(min_diff, numbers[i] + numbers[j])
            else:
                min_diff = min(min_diff, numbers[i] + numbers[j] - numbers[min_diff_index])
        if min_diff < min_diff:
            min_diff, min_diff_index = min_diff, i
    return numbers[min_diff_index], numbers[min_diff_index + 1]

