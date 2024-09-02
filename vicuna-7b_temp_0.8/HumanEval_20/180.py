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
        return (0, 0)
    smallest = numbers[0]
    smallest_idx = 0
    for idx, num in enumerate(numbers):
        if abs(num - smallest) < abs(smallest - smallest[smallest_idx % len(numbers)]):
            smallest, smallest_idx = idx, len(numbers) + idx
            if smallest_idx == len(numbers):
                smallest = smallest_idx + 1
    return (smallest, smallest_idx)