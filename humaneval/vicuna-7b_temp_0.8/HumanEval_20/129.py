from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    sorted_numbers = sorted(numbers)
    closest_pair = [(numbers[i], numbers[j]) for i in range(len(sorted_numbers)) for j in range(i + 1, len(sorted_numbers)) if abs(sorted_numbers[i] - sorted_numbers[j]) == abs(numbers[i] - numbers[j])]
    closest_pair = [(x, y) for x, y in closest_pair if len(set(x)) == 2]
    return closest_pair[0][0], closest_pair[0][1]

