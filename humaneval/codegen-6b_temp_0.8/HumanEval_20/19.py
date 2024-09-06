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
        raise ValueError("List provided is to small to search for closest numbers.")
    if len(numbers) == 2:
        return numbers[0], numbers[1]
    sort_numbers = sorted(numbers)
    closest_numbers = []
    for i in range(len(sort_numbers) - 1):
        closest_numbers.append((sort_numbers[i], sort_numbers[i + 1]))
    min_distance = closest_numbers[0][1] - closest_numbers[0][0]
    closest_elements = closest_numbers[0]
    for closest_pair in closest_numbers:
        if closest_pair[1] - closest_pair[0] < min_distance:
            min_distance = closest_pair[1] - closest_pair[0]
            closest_elements = closest_pair
    return closest_elements[0], closest_elements[1]

