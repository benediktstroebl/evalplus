from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    first = second = -1
    numbers.sort()
    for i, num in enumerate(numbers[1:]):
        if second == -1:
            second = num
            first = numbers[i]
        elif abs(first - num) < abs(second - num):
            second = num
        elif abs(first - num) > abs(second - num):
            first = num

    return first, second

