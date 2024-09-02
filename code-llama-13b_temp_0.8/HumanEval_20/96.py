from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    number_of_elements = len(numbers)
    min_distance = float('inf')
    number_1 = 0
    number_2 = 0

    for i in range(number_of_elements):
        for j in range(i, number_of_elements):
            if i == j:
                continue
            else:
                if abs(numbers[i] - numbers[j]) < min_distance:
                    number_1 = numbers[i]
                    number_2 = numbers[j]

    return number_1, number_2

