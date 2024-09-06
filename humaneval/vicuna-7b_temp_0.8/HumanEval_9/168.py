from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    def helper(numbers, max_index):
        if len(numbers) == 0:
            return [max_index]

        max_num = max(numbers)
        max_index = max_index + 1

        if max_index >= len(numbers):
            max_index = 0

        return helper(numbers[:max_index], max_index) + [max_num] + helper(numbers[max_index:], max_index + 1)

    return helper(numbers, 0)

