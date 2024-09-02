from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    closest = numbers[0]
    second = numbers[1]
    for i in range(2, len(numbers)):
        if abs(closest - numbers[i]) < abs(second - numbers[i]):
            second = closest
            closest = numbers[i]
        elif abs(closest - numbers[i]) == abs(second - numbers[i]):
            if closest < numbers[i]:
                closest = numbers[i]
            elif second > numbers[i]:
                second = numbers[i]
    return closest, second
