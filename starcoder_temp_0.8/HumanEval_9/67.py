from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    # Initialize an array of N-1 zeros to store the max element
    n = len(numbers)
    rolling_max = [0] * (n - 1)

    # Initialize the first max element
    rolling_max[0] = numbers[0]

    for i in range(1, n - 1):
        rolling_max[i] = max(numbers[i], rolling_max[i - 1])

    # Initialize the last max element
    rolling_max[n - 2] = max(numbers[n - 1], rolling_max[n - 2])

    return rolling_max

