from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    if len(numbers) == 2:
        return numbers[0], numbers[1]
    elif len(numbers) == 3:
        return min(numbers[0], numbers[1]), max(numbers[0], numbers[1])
    else:
        length = len(numbers)
        half = int(length / 2)
        first_half = numbers[:half]
        second_half = numbers[half:]
        result_first_half, result_second_half = find_closest_elements(first_half), find_closest_elements(
            second_half)
        distance_to_result_first_half, distance_to_result_second_half = \
            abs(numbers[half] - result_first_half[0]), abs(numbers[half] - result_second_half[0])
        if distance_to_result_first_half <= distance_to_result_second_half:
            return result_first_half
        else:
            return result_second_half

