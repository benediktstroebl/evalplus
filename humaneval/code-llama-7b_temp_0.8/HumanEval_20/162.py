from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    diff = float("inf")
    ans = (-1, -1)
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i == j:
                continue
            diff_between = abs(numbers[i] - numbers[j])
            if diff_between < diff:
                ans = (numbers[i], numbers[j])
                diff = diff_between
    return ans

