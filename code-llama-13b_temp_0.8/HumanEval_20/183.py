from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    min_ = numbers[0]
    max_ = numbers[0]
    min_index = 0
    max_index = 0

    for i in range(len(numbers)):
        if numbers[i] > max_:
            max_ = numbers[i]
            max_index = i
        if numbers[i] < min_:
            min_ = numbers[i]
            min_index = i
    if max_index < min_index:
        return min_, max_
    return max_, min_

