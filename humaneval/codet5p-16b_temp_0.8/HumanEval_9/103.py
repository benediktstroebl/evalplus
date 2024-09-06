from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    if len(numbers) < 2:
        return numbers

    rolling_max = [0] * len(numbers)
    rolling_max[0] = numbers[0]

    for index in range(1, len(numbers)):
        rolling_max[index] = max(numbers[index], rolling_max[index - 1])

    return rolling_max

