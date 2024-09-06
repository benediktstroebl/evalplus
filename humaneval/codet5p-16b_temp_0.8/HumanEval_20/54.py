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
        raise IndexError('Less than two elements given')
    diff = float('inf')
    first, second = numbers[0], numbers[1]
    for i, n in enumerate(numbers[1:]):
        if abs(n - numbers[i]) < diff:
            diff = abs(n - numbers[i])
            first, second = n, numbers[i]
    return first, second

