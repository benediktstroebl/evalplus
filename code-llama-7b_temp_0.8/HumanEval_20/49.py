from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    numbers = [float(x) for x in numbers]
    diff = min([abs(x - y) for x in numbers for y in numbers if x != y])
    ans = [(x, y) for x in numbers for y in numbers if x != y if abs(x - y) == diff]
    return (sorted(ans)[0][0], sorted(ans)[0][1])

