from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    nums = sorted(numbers)
    min_num = min(nums)
    max_num = max(nums)
    scale_num = (max_num - min_num) / 2
    scale_num = max_num if scale_num > max_num / 2 else min_num
    scaled_numbers = [scale_num * number if number < min_num else number - scale_num * (max_num - number) for number in nums]
    return scaled_numbers
