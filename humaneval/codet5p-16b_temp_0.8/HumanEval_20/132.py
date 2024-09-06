from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    diff_list = []
    for i in range(len(numbers) - 1):
        diff_list.append(numbers[i+1] - numbers[i])
    sorted_diff_list = sorted(diff_list)
    return (numbers[diff_list.index(sorted_diff_list[-1])], numbers[diff_list.index(sorted_diff_list[-2])])

