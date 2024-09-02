from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    first_distance = float("inf")
    second_distance = float("inf")
    first_elem = None
    second_elem = None
    for i in range(0, len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            first_distance = abs(numbers[i] - numbers[j])
            second_distance = abs(numbers[i] - numbers[j])
            if first_distance < second_distance:
                second_distance = first_distance
                second_elem = numbers[i]
                first_elem = numbers[j]
            else:
                second_distance = first_distance
                second_elem = numbers[j]
                first_elem = numbers[i]
    return first_elem, second_elem
    raise NotImplementedError()

