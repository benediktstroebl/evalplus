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

    for idx, num in enumerate(numbers[:-1]):
        if numbers[idx + 1] - num < abs(numbers[idx + 1] - numbers[-1]):
            first_num = num
            second_num = numbers[idx + 1]
            break
    else:
        # All else failed, return the last two elements
        first_num = numbers[-2]
        second_num = numbers[-1]
    return first_num, second_num
