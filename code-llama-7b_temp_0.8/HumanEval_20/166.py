from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    min_sum = numbers[1] - numbers[0]
    first_val = numbers[0]
    second_val = numbers[1]
    for index in range(len(numbers) - 1):
        first = numbers[index]
        second = numbers[index + 1]
        sum_val = second - first
        if min_sum > sum_val:
            first_val = first
            second_val = second
            min_sum = sum_val
    return first_val, second_val

