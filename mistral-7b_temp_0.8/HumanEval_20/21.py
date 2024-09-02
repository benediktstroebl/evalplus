from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    def get_closest(arr: List[float]) -> Tuple[float, float]:
        if len(arr) < 2:
            return (arr[0], arr[0])
        left, right = arr[0], arr[1]
        if right - left == min(right - i for i in arr[2:]):
            return (left, right)
        else:
            return get_closest(arr[1:])

    return get_closest(numbers)

