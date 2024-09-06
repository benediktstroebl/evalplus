from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    closest_1, closest_2 = min(numbers), max(numbers)
    closest_1_index, closest_2_index = numbers.index(closest_1), numbers.index(closest_2)

    if closest_1_index == closest_2_index:
        return closest_1, closest_2
    else:
        return numbers[closest_1_index], numbers[closest_2_index]

