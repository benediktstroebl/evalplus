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
        raise Exception("Less than 2 numbers")
    min_value = float('inf')
    min_index = -1
    min_other_index = -1

    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if abs(numbers[i] - numbers[j]) < min_value:
                min_value = abs(numbers[i] - numbers[j])
                min_index = i
                min_other_index = j
    return (numbers[min_index], numbers[min_other_index])

