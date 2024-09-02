from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    closest = 999999999999999
    min_1 = 999999999999999
    min_2 = 999999999999999
    for i in range(0, len(numbers)):
        for j in range(0, len(numbers)):
            if i != j:
                if numbers[j] - numbers[i] < closest:
                    closest = numbers[j] - numbers[i]
                    min_1 = numbers[i]
                    min_2 = numbers[j]
    return min_1, min_2

