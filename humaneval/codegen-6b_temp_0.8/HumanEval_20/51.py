from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    if len(numbers) < 2:
        raise ValueError("find_closest_elements needs at least two numbers!")
    number_list = numbers[:]
    number_list.sort()
    closest_pair = number_list[0], number_list[1]
    for i in range(2, len(numbers)):
        if abs(closest_pair[1] - closest_pair[0]) > abs(numbers[i] - closest_pair[0]):
            closest_pair = numbers[i], closest_pair[1]
        elif abs(closest_pair[1] - closest_pair[0]) < abs(numbers[i] - closest_pair[0]):
            closest_pair = closest_pair[0], numbers[i]
    return closest_pair

