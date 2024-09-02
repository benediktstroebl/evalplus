from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    sorted_numbers = sorted(numbers)
    left = sorted_numbers[0]
    right = sorted_numbers[-1]

    left_diff_list = [abs(left - num) for num in sorted_numbers]
    right_diff_list = [abs(right - num) for num in sorted_numbers]
    left_idx = left_diff_list.index(min(left_diff_list))
    right_idx = right_diff_list.index(min(right_diff_list))
    # print(left_idx)
    # print(right_idx)

    return sorted_numbers[left_idx], sorted_numbers[right_idx]

