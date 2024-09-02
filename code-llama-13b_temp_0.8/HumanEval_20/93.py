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
    closest_1 = numbers[0]
    closest_2 = numbers[1]
    for i in numbers:
        if i - closest_1 > closest_2 - i:
            closest_2 = i
        else:
            closest_1 = i
    if closest_1 == closest_2:
        return (closest_1, closest_1)
    else:
        return (closest_1, closest_2)

