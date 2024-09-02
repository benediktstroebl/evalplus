from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    l = len(numbers)
    if l < 2:
        raise Exception("List has to have at least two elements.")
    closest = numbers[0]
    index_closest = 0
    index_other = 0
    for i in range(1, l):
        if abs(numbers[i] - numbers[index_closest]) < abs(numbers[i] - numbers[index_other]):
            closest = numbers[i]
            index_closest = i
        else:
            index_other = i
    return closest, numbers[index_closest]

