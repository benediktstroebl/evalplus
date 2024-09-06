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
        raise ValueError('not enough elements')
    min_index_1, min_index_2 = 0, 1
    min_value_1, min_value_2 = numbers[0], numbers[1]
    for index_1 in range(len(numbers) - 1):
        for index_2 in range(index_1 + 1, len(numbers)):
            if abs(numbers[index_1] - numbers[index_2]) < abs(min_value_1 - min_value_2):
                min_value_1, min_value_2 = numbers[index_1], numbers[index_2]
                min_index_1, min_index_2 = index_1, index_2
    return (min_value_1, min_value_2)
