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
        return (numbers[0], numbers[0])
    max_diff = max(numbers) - min(numbers)
    min_diff = max(numbers) - min(numbers)
    min_diff_index = 0
    closest_numbers = numbers[0]
    for index, number in enumerate(numbers[1:]):
        difference = number - closest_numbers
        if difference < min_diff:
            min_diff = difference
            min_diff_index = index
        elif difference == min_diff:
            if abs(closest_numbers - numbers[0]) < abs(number - numbers[0]):
                min_diff_index += 1
            else:
                min_diff_index = 0
        else:
            if abs(closest_numbers - numbers[0]) < abs(number - numbers[0]):
                min_diff_index += 1
            else:
                closest_numbers = number
    return min_diff_index, closest_numbers

