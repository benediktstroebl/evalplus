from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    if len(numbers) == 2:
        return (numbers[0], numbers[1])
    else:
        closest = min(enumerate(numbers), key=lambda x: abs(x[1] - numbers[0]))
        numbers.remove(numbers[0])
        numbers.remove(closest[1])
        return (closest[1], min(numbers, key=lambda x: abs(x - closest[1])))

