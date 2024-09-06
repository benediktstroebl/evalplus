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
        raise ValueError('list must contain at least two numbers')

    sorted_numbers = sorted(numbers)
    closest_to_median = sorted_numbers[len(sorted_numbers) // 2]
    closest = sorted_numbers[0]
    closest_index = numbers.index(closest)
    for i in range(1, len(numbers)):
        if abs(numbers[i] - closest_to_median) < abs(numbers[i] - closest):
            closest = numbers[i]
            closest_index = i

    return closest, closest_index

