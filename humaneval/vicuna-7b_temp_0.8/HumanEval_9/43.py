from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    current_max = None
    result = []
    for i in range(0, len(numbers) - 1, 3):
        nums = numbers[i:i + 3]
        if nums[0] == current_max:
            result.append(nums[0])
        else:
            if current_max is not None:
                result.append(current_max)
            result.append(nums[0])
            current_max = nums[0]
    result.append(current_max)
    return result

