from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    if len(numbers) < 1:
        raise ValueError("Please provide at least 2 numbers.")
    if len(numbers) == 1:
        return numbers[0], numbers[0]
    sorted_list = sorted(numbers)
    left_half_index = 0
    right_half_index = len(numbers) - 1
    left_num = sorted_list[0]
    right_num = sorted_list[-1]
    if abs(left_num - right_num) == 0.0:
        return left_num, right_num
    while True:
        if left_half_index >= right_half_index:
            if abs(left_num - right_num) > abs(left_num - sorted_list[right_half_index]):
                return left_num, sorted_list[right_half_index]
            return right_num, left_num
        mid_point = int((left_half_index + right_half_index) / 2)
        mid_num = sorted_list[mid_point]
        if abs(left_num - right_num) > abs(left_num - mid_num):
            left_num = mid_num
        else:
            right_num = mid_num

