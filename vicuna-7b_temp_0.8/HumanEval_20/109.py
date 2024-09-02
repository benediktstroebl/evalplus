from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    def distance(a, b):
        return math.sqrt((a - b) ** 2)

    closest_elements = []
    min_distance = math.inf
    min_index = 0
    for i in range(len - 1):
        for j in range(i + 1, len):
            distance_ = distance(numbers[i], numbers[j])
            if distance_ < min_distance:
                min_distance = distance_
                min_index = j
    return numbers[min_index], numbers[min_index + 1]

