from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    min1, min2 = numbers[0], numbers[1]
    for i in range(2, len(numbers)):
        if numbers[i] < min1:
            min2 = min1
            min1 = numbers[i]
        elif numbers[i] < min2:
            min2 = numbers[i]
    return (min1, min2)
