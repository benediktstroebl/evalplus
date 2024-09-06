from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # TODO: implement this function
    min_distance = None
    index = 0
    min_index = 0
    for i in range(0, len(numbers)):
        temp_distance = numbers[i] - numbers[i - 1]
        if min_distance is None:
            min_distance = temp_distance
        if abs(temp_distance) < min_distance:
            min_distance = temp_distance
            index = i
    return numbers[index - 1], numbers[index]

