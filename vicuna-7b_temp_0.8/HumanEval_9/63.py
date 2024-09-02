from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    def helper(numbers, moment, max_found):
        if len(numbers) == 0:
            return [max_found] * len(numbers)
        if len(numbers) == 1:
            return [max_found]
        else:
            max_found = numbers[0]
            for i in range(moment, len(numbers)):
                numbers.remove(numbers[i])
            return helper(numbers, moment + 1, max_found) + helper(numbers, moment, max_found)
    return helper(numbers, 0, [])

