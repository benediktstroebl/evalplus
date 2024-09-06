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
        return numbers[0], numbers[0]

    closest_num1 = numbers[0]
    closest_num2 = numbers[0]
    min_dist_num = numbers[0]
    for num in numbers[1:]:
        dist = abs(num - closest_num1) + abs(num - closest_num2)
        if dist < min_dist_num:
            min_dist_num = dist
            closest_num1, closest_num2 = num, num

    return closest_num1, closest_num2

