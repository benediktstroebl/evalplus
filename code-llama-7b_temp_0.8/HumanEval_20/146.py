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
        raise Exception("Not enough numbers to find the closest ones")

    min_dif = float("inf")
    min_idx_1 = min_idx_2 = 0

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            dif = abs(numbers[i] - numbers[j])
            if dif < min_dif:
                min_dif = dif
                min_idx_1 = i
                min_idx_2 = j

    return numbers[min_idx_1], numbers[min_idx_2]

