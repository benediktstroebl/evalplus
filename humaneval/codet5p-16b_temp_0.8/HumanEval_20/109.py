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
        raise Exception('Please supply at least 2 numbers to work with')
    min_num = min(numbers)
    max_num = max(numbers)
    min_abs_diff = abs(numbers[0] - numbers[1])
    closest = [min_num, min_num]
    for i in range(1, len(numbers)):
        diff = abs(numbers[i] - numbers[i - 1])
        if diff < min_abs_diff:
            closest[1] = closest[0]
            closest[0] = numbers[i - 1]
            min_abs_diff = diff
        elif diff == min_abs_diff:
            closest.append(numbers[i - 1])
            closest.append(numbers[i])
    return tuple(closest)
    pass
