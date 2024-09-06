from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    min_diff = float('inf')

    min_number = float('inf')
    max_number = float('-inf')
    for number in numbers:
        if min_number > number:
            min_number = number
        if max_number < number:
            max_number = number

    numbers = [number for number in numbers if (max_number - number) <= (number - min_number)]
    if len(numbers) == 1:
        return min_number, max_number
    elif len(numbers) == 0:
        return float('inf'), float('-inf')
    else:
        for number in numbers:
            difference = abs(min_number - number)
            if difference < min_diff:
                min_diff = difference
                result_number = number
        return min_number, result_number
