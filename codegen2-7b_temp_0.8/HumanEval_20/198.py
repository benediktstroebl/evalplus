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
        raise ValueError('The supplied list must contain at least two elements')
    closest_numbers = [None, None]
    for i in range(len(numbers)):
        if closest_numbers[0] is None or numbers[i] < closest_numbers[0]:
            closest_numbers[0] = numbers[i]
        if closest_numbers[1] is None or numbers[i] > closest_numbers[1]:
            closest_numbers[1] = numbers[i]
    return closest_numbers[0], closest_numbers[
