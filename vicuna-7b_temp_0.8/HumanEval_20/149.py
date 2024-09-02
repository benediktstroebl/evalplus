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
        return None

    distances = [math.sqrt((numbers[i] - numbers[j]) ** 2) for i in range(n-1) for j in range(i+1, n)]
    min_distance = min(distances)
    closest_pair = [(i, j) for i in range(n-1) for j in range(i+1, n) if math.fabs(numbers[i] - numbers[j]) < min_distance/1000.]

    closest_pair_index = [closest_pair.index(p) for p in closest_pair]
    closest_pair = [numbers[i] for i in closest_pair_index]

    return closest_pair[0], closest_pair[1]

