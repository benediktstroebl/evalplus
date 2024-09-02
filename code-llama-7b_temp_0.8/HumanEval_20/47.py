from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    numbers_len = len(numbers)
    if numbers_len < 2:
        raise ValueError('Length of numbers must be at least 2')

    min_delta = float('inf')
    min_pair = (0, 1)
    for i in range(numbers_len - 1):
        for j in range(i + 1, numbers_len):
            delta = abs(numbers[i] - numbers[j])
            if delta < min_delta:
                min_delta = delta
                min_pair = (i, j)

    return numbers[min_pair[0]], numbers[min_pair[1]]

