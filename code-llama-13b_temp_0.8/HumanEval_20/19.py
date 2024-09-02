from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    numbers = sorted(numbers)
    number_1 = numbers[0]
    number_2 = numbers[1]
    differences = []
    for number in numbers:
        difference = number_1 - number_2
        differences.append(difference)
        if difference < 0:
            number_1 = number
        elif difference > 0:
            number_2 = number
        else:
            return number_1, number_2
    return number_1, number_2

