from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    min_diff = 1000000000000
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                abs_diff = abs(numbers[i] - numbers[j])
                if abs_diff < min_diff:
                    min_diff = abs_diff
                    smallest, largest = numbers[i], numbers[j]
                    if numbers[i] > numbers[j]:
                        smallest, largest = numbers[j], numbers[i]
    return smallest, largest

