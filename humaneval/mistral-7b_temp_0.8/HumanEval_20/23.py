from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    numbers.sort()
    if len(numbers) < 2:
        raise ValueError('Must supply at least two numbers')
    if len(numbers) == 2:
        return numbers[0], numbers[1]
    closest_numbers = numbers[0], numbers[1]
    for number in numbers[2:]:
        if abs(number - closest_numbers[0]) < abs(number - closest_numbers[1]):
            closest_numbers = closest_numbers[1], number
        elif abs(number - closest_numbers[0]) == abs(number - closest_numbers[1]):
            closest_numbers = number, closest_numbers[0]
    return closest_numbers
