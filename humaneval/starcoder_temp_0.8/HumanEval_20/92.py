from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # Here's an example of what the 'zip' function does:
    # >>> list(zip([1, 2, 3], ['a', 'b', 'c']))
    # [(1, 'a'), (2, 'b'), (3, 'c')]
    first_two = zip(numbers, numbers[1:])
    return min(first_two, key=lambda x: abs(x[0] - x[1]))

