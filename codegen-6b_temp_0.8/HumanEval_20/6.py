from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    closest_elements = []
    for index in range(len(numbers) - 1):
        if index == 0:
            closest_elements.append(min(numbers[0], numbers[1]))
            closest_elements.append(max(numbers[0], numbers[1]))
            continue
        the_lowest = min(closest_elements[index - 1], numbers[index], numbers[index + 1])
        the_highest = max(closest_elements[index - 1], numbers[index], numbers[index + 1])
        closest_elements.append(the_lowest)
        closest_elements.append(the_highest)
    return closest_elements[-1], closest_elements[-2]

