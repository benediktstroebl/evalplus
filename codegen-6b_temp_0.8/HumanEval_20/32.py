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
        raise ValueError('Less than 2 numbers given')
    target = 0.0
    diff = abs(numbers[0] - numbers[1])
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            curr_diff = abs(numbers[i] - numbers[j])
            if curr_diff < diff:
                target = numbers[i]
                diff = curr_diff
            elif curr_diff == diff:
                target = min(target, numbers[i], numbers[j])

    return target, target

