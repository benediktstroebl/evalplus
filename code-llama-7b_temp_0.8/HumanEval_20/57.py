from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # Find min
    min_diff = numbers[1] - numbers[0]
    min_index = 0
    for i, num in enumerate(numbers[1:], 1):
        if num - numbers[i - 1] < min_diff:
            min_diff = num - numbers[i - 1]
            min_index = i
    # Find max
    max_diff = numbers[min_index + 1] - numbers[min_index]
    max_index = min_index + 1
    for i in range(min_index + 1, len(numbers)):
        if numbers[i] - numbers[max_index] < max_diff:
            max_diff = numbers[i] - numbers[max_index]
            max_index = i
    return numbers[min_index], numbers[max_index]

