from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    nums = numbers[:]
    min_num = min(nums)
    max_num = max(nums)
    for i, num in enumerate(nums):
        if num < min_num:
            nums[i] = 0.0
        elif num > max_num:
            nums[i] = 1.0
    return nums

