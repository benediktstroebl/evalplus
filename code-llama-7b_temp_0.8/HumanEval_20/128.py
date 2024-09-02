from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    closest_number = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            number1 = numbers[i]
            number2 = numbers[j]
            if abs(number1 - number2) < abs(closest_number[0] - closest_number[1]):
                closest_number = [number1, number2]
    return (closest_number[0], closest_number[1])

