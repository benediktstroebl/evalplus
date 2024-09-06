from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    min_dif = abs(numbers[0] - numbers[1])
    closest = [numbers[0], numbers[1]]
    numbers.sort()
    for number in numbers:
        for number2 in numbers:
            if abs(number - number2) < min_dif and number != number2:
                min_dif = abs(number - number2)
                closest = [number, number2]
    closest.sort()
    return closest[0], closest[1]

