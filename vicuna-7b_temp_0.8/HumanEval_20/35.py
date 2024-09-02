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
        return numbers[0], numbers[0]

    best_sum = numbers[0]
    best_index = 0

    for i in range(1, len(numbers)):
        for j in range(i + 1, len(numbers)):
            diff = numbers[i] - numbers[j]
            sum = best_sum + diff
            if sum < best_sum:
                best_sum = sum
                best_index = j

    return numbers[best_index], numbers[best_index + 1]

