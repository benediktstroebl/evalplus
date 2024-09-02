from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    min_number, max_number = numbers[0], numbers[1]
    min_number_index, max_number_index = 0, 1
    for i in range(2, len(numbers)):
        if numbers[i] < min_number:
            min_number = numbers[i]
            min_number_index = i
        elif numbers[i] > max_number:
            max_number = numbers[i]
            max_number_index = i
    return (min_number, numbers[max_number_index]), (max_number, numbers[min_number_index])

