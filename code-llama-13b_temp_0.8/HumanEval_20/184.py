from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    closest_nums: List[Tuple[float, float]] = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            closest_nums.append((abs(numbers[i] - numbers[j]), numbers[i], numbers[j]))
    return sorted(closest_nums)[0][1:]

