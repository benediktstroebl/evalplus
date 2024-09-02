from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    n = len(numbers)
    if n < 2:
        raise ValueError("List needs to have at least two elements")
    if n == 2:
        return (min(numbers), max(numbers))
    if n == 3:
        return min(numbers), max(numbers[1], numbers[2])
    if n == 4:
        return min(numbers[2], numbers[3]), max(numbers[2], numbers[3])
    if n == 5:
        return min(numbers[3], numbers[4]), max(numbers[3], numbers[4])

    middle = n // 2
    left_num = numbers[middle - 1]
    right_num = numbers[middle - 1]
    left_dif = abs(left_num - numbers[middle])
    right_dif = abs(right_num - numbers[middle])
    for i in xrange(middle - 1, -1, -1):
        if abs(numbers[i] - left_num) < left_dif:
            left_dif = abs(numbers[i] - left_num)
            left_num = numbers[i]
        elif abs(numbers[i] - right_num) < right_dif:
            right_dif = abs(numbers[i] - right_num)
            right_num = numbers[i]

    if left_dif < right_dif:
        return left_num, right_num
    else:
        return right_num, left_num

