from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    numbers_length = len(numbers)
    closest_one = numbers[0]
    closest_two = numbers[0]

    if numbers_length > 1:
        for num in numbers[1:]:
            if abs(num - closest_one) < abs(num - closest_two):
                closest_one = num
            else:
                closest_two = num

    return closest_one, closest_
