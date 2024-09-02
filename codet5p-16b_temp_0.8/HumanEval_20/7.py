from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    if len(numbers) <= 1:
        raise ValueError("List must contain at least two elements")

    min_diff = None
    first_num = None
    second_num = None

    for i, num in enumerate(numbers):
        for j, num2 in enumerate(numbers):
            if j <= i:
                continue

            diff = abs(num2 - num)
            if (min_diff is None) or (diff < min_diff):
                min_diff = diff
                first_num = num
                second_num = num2

    return (first_num, second_num)
    
