from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    nums = list(enumerate(numbers))
    nums.sort(key=lambda item: item[1])
    index1 = 0
    index2 = 1
    while index1 + 1 < len(nums):
        if abs(nums[index1][1] - nums[index2][1]) < abs(nums[index1][1] - nums[index1 + 2][1]):
            index1 += 1
            index2 += 1
        else:
            index1 += 2
    return nums[index1][1], nums[index2][1]

