from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    closest_pair = (numbers[0], numbers[1])
    diff = abs(numbers[0] - numbers[1])
    for i, num in enumerate(numbers[2:]):
        if i % 2 == 1:
            diff2 = abs(closest_pair[0] - num)
            if diff2 < diff:
                closest_pair = (closest_pair[0], num)
            else:
                closest_pair = (num, closest_pair[1])
    return closest_pair

