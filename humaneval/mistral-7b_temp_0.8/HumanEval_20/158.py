from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    if len(numbers) <= 1:
        raise ValueError("list has to have more than 1 element")
    numbers = sorted(numbers)
    if len(numbers) == 2:
        return numbers[0], numbers[1]
    closest = numbers[1] - numbers[0]
    current = numbers[2] - numbers[1]
    for i in range(3, len(numbers)):
        if current < closest:
            closest = current
            return numbers[i - 2], numbers[i]
        current = numbers[i] - numbers[i - 1]
    return numbers[-2], numbers[-1]
