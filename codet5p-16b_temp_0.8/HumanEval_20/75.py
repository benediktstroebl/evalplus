from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    for index1 in range(len(numbers)):
        for index2 in range(index1 + 1, len(numbers)):
            if numbers[index1] < numbers[index2]:
                return (numbers[index1], numbers[index2])
            else:
                return (numbers[index2], numbers[index1])

