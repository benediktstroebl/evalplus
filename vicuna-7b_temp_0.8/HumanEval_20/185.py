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
        return (float("inf"), float("-inf"))
    closest_values = []
    closest_numbers = []
    for value in numbers:
        closest_values.append(distance(numbers[0], value))
        for i in range(1, len(numbers)):
            if abs(numbers[i] - value) < abs(numbers[i] - numbers[i - 1]):
                numbers[i] = value
                closest_numbers.append(numbers[i])
        for i in range(1, len(numbers)):
            if abs(numbers[i] - value) < abs(numbers[i] - numbers[i - 1]):
                numbers[i] = value
                closest_numbers.append(numbers[i])
    closest_numbers.sort()
    closest_values.sort()
    return closest_numbers[0], closest_numbers[closest_numbers.index(closest_numbers.sort()[0])]

