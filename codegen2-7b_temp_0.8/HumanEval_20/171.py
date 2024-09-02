from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    distances = [abs(x - numbers[0]) for x in numbers]
    min_idx = distances.index(min(distances))

    if min_idx!= 0:
        return numbers[min_idx], numbers[0]

    if min_idx!= len(numbers) - 1:
        return numbers[min_idx], numbers[min_idx + 1]

    return numbers[min_idx], numbers[0]
