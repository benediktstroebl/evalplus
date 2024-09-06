from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    if numbers.__len__() < 2:
        raise ValueError("list must contain at least two numbers")
    numbers.sort()
    ref_num = numbers.pop()
    candidate_1 = numbers.pop()
    if candidate_1 - ref_num < ref_num - candidate_1:
        candidate_2 = numbers.pop()
    else:
        candidate_2 = candidate_1
    return ref_num, candidate_2

