from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    assert len(numbers) >= 2, "List must be of length >= 2"

    min_distance = 100000000000000
    result_1 = -1
    result_2 = -1

    for index_1, number_1 in enumerate(numbers):
        for index_2, number_2 in enumerate(numbers):
            if index_1 != index_2:
                distance = abs(number_1 - number_2)
                if distance < min_distance:
                    min_distance = distance
                    result_1 = number_1
                    result_2 = number_2

    if result_1 < result_2:
        return result_1, result_2
    else:
        return result_2, result_1

