from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        return []
    current_max = numbers[0]
    current_nums = numbers[:]
    for i in range(1, len(current_nums)):
        if current_nums[i] > current_max:
            current_max = current_nums[i]
        else:
            current_nums[i:i+1] = [current_max] + current_nums[i+1:]
            current_max = current_nums[i]
    return current_nums[1:]

