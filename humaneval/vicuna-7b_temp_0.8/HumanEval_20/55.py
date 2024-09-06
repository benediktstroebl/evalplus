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
    closest_index1 = 0
    closest_index2 = 1

    for i in range(1, len(numbers)):
        difference1 = numbers[closest_index1] - numbers[closest_index2]
        difference2 = numbers[i] - numbers[closest_index1]
        distance = difference1**2 + difference2**2

        if distance <= (numbers[closest_index1] - numbers[i]):
            closest_index1 = i
            closest_index2 = closest_index1

    return numbers[closest_index1], numbers[closest_index2]

