from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    nums = sorted(numbers)
    num_len = len(nums)
    closest_num = nums[0]
    second_closest_num = nums[num_len - 1]
    for i in range(num_len):
        if abs(nums[i] - closest_num) < abs(second_closest_num - closest_num):
            second_closest_num = closest_num
            closest_num = nums[i]
        elif abs(nums[i] - closest_num) > abs(second_closest_num - closest_num):
            second_closest_num = nums[i]
        elif i == num_len - 1:
            second_closest_num = nums[i]
    return closest_num, second_closest_num

