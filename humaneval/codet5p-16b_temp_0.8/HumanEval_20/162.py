from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    if numbers[0] > numbers[1]:
        min_n, max_n = numbers[0], numbers[1]
    else:
        min_n, max_n = numbers[1], numbers[0]

    for num in numbers[2:]:
        if num > max_n:
            max_n = num
        elif num < min_n:
            min_n = num
        else:
            continue

    return (min_n, max_n)
