from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    n = len(numbers)
    window_size = 1
    rolling_max = numbers[:]
    for i in range(n):
        window_size = max(0, window_size - 1)
        rolling_max[i:i+window_size] = [max(vals) for vals in rolling_max[i:i+window_size]]
    return rolling_max[n-1:]
