from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    min_dist = None
    min_1 = None
    min_2 = None
    for idx, num in enumerate(numbers):
        for compare_idx, compare_num in enumerate(numbers):
            if idx == compare_idx:
                continue
            if min_dist is None or abs(num - compare_num) < min_dist:
                if min_dist is not None:
                    if abs(num - compare_num) < min_dist:
                        min_1 = min_2
                        min_2 = min_dist
                        min_dist = abs(num - compare_num)
                    else:
                        min_1 = min_dist
                        min_dist = abs(num - compare_num)
                        min_2 = min_1
                else:
                    min_1 = num
                    min_2 = compare_num
                    min_dist = abs(num - compare_num)
    return min_1, min_2
