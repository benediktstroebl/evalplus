from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    n = len(numbers)
    if n < 2:
        return n, n

    closest_pairs = []
    closest_pair = (numbers[0], numbers[0])
    for i in range(1, n):
        for j in range(i + 1, n):
            dist = abs(numbers[i] - numbers[j])
            if dist < abs(closest_pair[0] - closest_pair[1]):
                closest_pair = (numbers[j], numbers[i])
                dist = abs(closest_pair[0] - closest_pair[1])
            closest_pairs.append(closest_pair)

    return max(closest_pairs, key=lambda x: abs(x[1] - x[0])), max(closest_pairs, key=lambda x: abs(x[0] - x[1]))

