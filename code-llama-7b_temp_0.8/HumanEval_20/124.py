from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    best_pair = (numbers[0], numbers[1])
    best_diff = abs(numbers[0] - numbers[1])

    for i in range(1, len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if i == j:
                continue

            candidate_pair = (numbers[i], numbers[j])
            candidate_diff = abs(numbers[i] - numbers[j])

            if candidate_diff < best_diff:
                best_diff = candidate_diff
                best_pair = candidate_pair

    return best_pair

