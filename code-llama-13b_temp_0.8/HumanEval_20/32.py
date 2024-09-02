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
        raise ValueError("List needs to have at least 2 items")
    numbers = sorted(numbers)
    if len(numbers) == 2:
        return tuple(numbers)
    else:
        min_diff = abs(numbers[0] - numbers[1])
        for i in range(0, len(numbers) - 1):
            if abs(numbers[i] - numbers[i + 1]) < min_diff:
                min_diff = abs(numbers[i] - numbers[i + 1])
                first_number = numbers[i]
                second_number = numbers[i + 1]
        return first_number, second_number

