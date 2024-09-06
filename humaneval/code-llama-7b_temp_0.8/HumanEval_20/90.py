from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    min_diff = float("inf")
    left_closest = float("inf")
    right_closest = float("-inf")

    for index in range(1, len(numbers)):
        left_num = numbers[index - 1]
        right_num = numbers[index]
        diff = abs(left_num - right_num)

        if diff <= min_diff:
            min_diff = diff
            left_closest = left_num
            right_closest = right_num

    return left_closest, right_closest

