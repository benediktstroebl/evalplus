from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_val = numbers[0]
    nums = numbers[:]

    running_max = [max_val]

    for i in range(1, len(nums)):
        if nums[i] > max_val:
            max_val = nums[i]
        else:
            running_max.append(max_val)
            max_val = nums[i]

    return running_max