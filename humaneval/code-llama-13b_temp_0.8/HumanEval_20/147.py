from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    numbers.sort()
    index_a = 0
    index_b = 1
    while index_b < len(numbers):
        if numbers[index_b] - numbers[index_a] < numbers[index_b + 1] - numbers[index_a]:
            break
        index_a += 1
        index_b += 1
    return numbers[index_a], numbers[index_b]

