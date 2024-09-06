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

    min_index = 0
    max_index = len(numbers) - 1
    min_distance = max_distance = float("inf")

    for index in range(len(numbers)):
        if index == min_index or index == max_index:
            continue

        if abs(numbers[index] - numbers[min_index]) < min_distance:
            min_index = index
            min_distance = abs(numbers[index] - numbers[min_index])

        if abs(numbers[index] - numbers[max_index]) < max_distance:
            max_index = index
            max_distance = abs(numbers[index] - numbers[max_index])

    return numbers[min_index], numbers[max_index]

