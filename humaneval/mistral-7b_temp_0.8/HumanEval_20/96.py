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
        raise ValueError("List must contain at least two elements")
    else:
        closest = numbers[0]
        closest_other = numbers[1]
        for index, value in enumerate(numbers):
            if index > 0:
                distance = abs(numbers[index] - numbers[index-1])
                if distance < abs(closest - closest_other):
                    closest = numbers[index-1]
                    closest_other = numbers[index]
        return closest, closest_other
