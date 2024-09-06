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
        raise ValueError('length of numbers has to be at least 2')

    closest_numbers = []

    for idx, number in enumerate(numbers):
        closest_numbers.append((number, abs(number - numbers[idx - 1])))

    closest_numbers.sort(key=lambda tup: tup[1])

    return closest_numbers[0], closest_numbers[-1]

