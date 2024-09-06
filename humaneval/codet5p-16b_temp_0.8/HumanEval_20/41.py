from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    min_num = numbers[0]
    min_index = 0
    for i in range(len(numbers)):
        if numbers[i] < min_num:
            min_num = numbers[i]
            min_index = i

    max_num = numbers[0]
    max_index = 0
    for i in range(len(numbers)):
        if numbers[i] > max_num:
            max_num = numbers[i]
            max_index = i

    return (min_num, max_num)

