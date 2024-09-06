from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    largest_diff = None
    choice_1 = None
    choice_2 = None

    # order the list by absolute difference from the median
    ordered = sorted(numbers)
    sorted_len = len(ordered)
    median_index = sorted_len // 2
    if sorted_len % 2 == 0:
        median_index1 = median_index - 1
        median_index2 = median_index
    else:
        median_index1 = median_index
        median_index2 = median_index + 1

    median1 = ordered[median_index1]
    median2 = ordered[median_index2]
    for index, number in enumerate(ordered):
        diff = abs(number - median1)
        if largest_diff is None or diff < largest_diff:
            choice_1 = number
            choice_2 = median1
            largest_diff = diff
        if diff < abs(number - median2):
            choice_1 = number
            choice_2 = median2
            largest_diff = diff
    return (choice_1, choice_2)

