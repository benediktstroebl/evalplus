from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    numbers = sorted(numbers)
    min_diff = numbers[1] - numbers[0]
    min_diff_pair = (numbers[0], numbers[1])
    for index in range(len(numbers) - 1):
        num1 = numbers[index]
        num2 = numbers[index + 1]
        if abs(num1 - num2) < min_diff:
            min_diff = abs(num1 - num2)
            min_diff_pair = (num1, num2)
    return min_diff_pair

