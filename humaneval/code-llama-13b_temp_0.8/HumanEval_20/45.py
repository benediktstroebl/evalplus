from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    sorted_numbers = sorted(numbers)
    index_1 = 0
    index_2 = 1
    min_diff = abs(sorted_numbers[index_1] - sorted_numbers[index_2])
    for index_1, number in enumerate(sorted_numbers):
        if index_1 != index_2:
            diff = abs(number - sorted_numbers[index_2])
            if diff < min_diff:
                min_diff = diff
                if sorted_numbers[index_1] > sorted_numbers[index_2]:
                    temp = sorted_numbers[index_1]
                    sorted_numbers[index_1] = sorted_numbers[index_2]
                    sorted_numbers[index_2] = temp
            else:
                break
    return sorted_numbers[index_1], sorted_numbers[index_2]

