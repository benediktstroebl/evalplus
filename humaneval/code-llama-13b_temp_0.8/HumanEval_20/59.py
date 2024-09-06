from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    lowest_diff = numbers[1] - numbers[0]
    smallest_num = numbers[0]
    largest_num = numbers[0]
    for i in range(1, len(numbers)):
        for j in range(0, len(numbers) - i):
            if abs(numbers[j] - numbers[j + 1]) < lowest_diff:
                lowest_diff = abs(numbers[j] - numbers[j + 1])
                smallest_num = numbers[j]
                largest_num = numbers[j + 1]
    return smallest_num, largest_num

