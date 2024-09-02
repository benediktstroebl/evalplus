from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    current_smallest_diff = abs(numbers[0] - numbers[1])
    smallest_diff = current_smallest_diff
    smallest_diff_index1 = 0
    smallest_diff_index2 = 1
    for index1, num1 in enumerate(numbers):
        for index2, num2 in enumerate(numbers[index1:]):
            current_smallest_diff = abs(num1 - num2)
            if current_smallest_diff < smallest_diff:
                smallest_diff = current_smallest_diff
                smallest_diff_index1 = index1
                smallest_diff_index2 = index2 + index1
    return numbers[smallest_diff_index1], numbers[smallest_diff_index2]

