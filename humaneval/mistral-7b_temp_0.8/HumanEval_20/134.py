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

    min_max_nums = [nums[0], nums[-1]]

    for i in range(len(nums)):
        if i == 0:
            continue
        if i == len(nums) - 1:
            continue
        if abs(nums[i] - min_max_nums[0]) < abs(nums[i] - min_max_nums[1]):
            min_max_nums[1] = nums[i]
        elif abs(nums[i] - min_max_nums[0]) > abs(nums[i] - min_max_nums[1]):
            min_max_nums[0] = nums[i]
        elif abs(nums[i] - min_max_nums[0]) == abs(nums[i] - min_max_nums[1]):
            if nums[i] < min_max_nums[0]:
                min_max_nums[0] = nums[
