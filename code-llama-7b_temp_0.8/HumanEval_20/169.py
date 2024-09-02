from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    result = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            diff = abs(numbers[i] - numbers[j])
            if diff < 1e-10:
                result.append((numbers[i], numbers[j]))
    result.sort(key=lambda x: (x[0], x[1]))
    return result[0]

