from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    min_difference = numbers[1] - numbers[0]
    min_1 = 0
    min_2 = 0
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i < j and numbers[i] - numbers[j] < min_difference:
                min_difference = numbers[i] - numbers[j]
                min_1 = i
                min_2 = j
    return (numbers[min_1], numbers[min_2])

