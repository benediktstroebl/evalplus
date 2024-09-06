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
        raise ValueError("List must contain at least two numbers")
    min_diff = abs(numbers[0] - numbers[1])
    diff = 0
    min_pair = (numbers[0], numbers[1])
    for i, num in enumerate(numbers):
        if i == len(numbers) - 1:
            break
        next_num = numbers[i + 1]
        diff = abs(num - next_num)
        if diff < min_diff:
            min_diff = diff
            min_pair = (num, next_num)
    return min_pair

