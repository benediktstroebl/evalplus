from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    closest_pair = []
    closest_distance = float("inf")
    for num in numbers:
        d = float("inf")
        for i in range(len(numbers) - 1):
            d = min(d, abs(num - numbers[i])) + abs(num - numbers[i + 1])
        if d < closest_distance:
            closest_pair = [num, numbers[i]]
            closest_distance = d
    return closest_pair[0], closest_pair[1]