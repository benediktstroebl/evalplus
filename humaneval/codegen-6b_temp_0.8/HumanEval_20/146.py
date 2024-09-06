from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    sorted_list = sorted(numbers)
    closest_pairs = tuple()
    for i in range(len(sorted_list) - 1):
        if sorted_list[i] == sorted_list[i+1]:
            continue
        next_num = sorted_list[i+1]
        prev_num = sorted_list[i]
        if abs(prev_num - next_num) < abs(prev_num - closest_pairs[0]):
            closest_pairs = (prev_num, next_num)
        elif abs(prev_num - next_num) == abs(prev_num - closest_pairs[0]):
            closest_pairs = (prev_num, next_num)
    return closest_pairs


import unittest

