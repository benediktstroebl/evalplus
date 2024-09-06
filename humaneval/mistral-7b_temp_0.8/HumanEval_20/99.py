from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    # Smallest and largest elements of numbers
    min_num = min(numbers)
    max_num = max(numbers)

    if (max_num - min_num) <= 1:
        return (min_num, max_num)

    # Find the closest two elements in numbers
    min_diff = 10 ** 99
    min_1, min_2 = None, None
    for num in numbers:
        diff = abs(num - min_num)
        if diff < min_diff:
            min_diff = diff
            min_2 = min_1
            min_1 = num

    return (min_1, min_2)
