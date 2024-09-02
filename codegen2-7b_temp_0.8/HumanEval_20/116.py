from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    smaller: List[float] = []
    larger: List[float] = []
    for n in numbers:
        if n in smaller:
            larger.append(n)
        else:
            smaller.append(n)
    if len(larger) == 0:
        return numbers[0], numbers[1]
    elif len(larger) == 1:
        return smaller[0], larger[0]
    else:
        return smaller[0], larger[0] if smaller[0] < larger[0] else smaller[1]
