from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # TODO: assert that the numbers are NOT negative
    result = []
    i = 0
    # iterate over the list of numbers, and for each number, append the max element to the result list
    # at the moment we have no idea where the next max element is, so we simply append the current number
    while i < len(numbers):
        result.append(max(numbers[len(numbers) - 1 - i:len(numbers) - i]))
        i += 1
    return result

