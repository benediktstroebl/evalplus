from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    closest_pair = [(max(x, key=lambda x: abs(x - smallest)), smallest) for smallest, largest in zip(numbers, numbers[1:])]
    if len(closest_pair) == 1:
        return closest_pair[0][0], closest_pair[0][1]
    elif len(closest_pair) == 2:
        return closest_pair[0][0], closest_pair[1][0]
    else:
        raise ValueError("More than one closest pair found")

