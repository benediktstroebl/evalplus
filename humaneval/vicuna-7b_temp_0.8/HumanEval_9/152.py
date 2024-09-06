from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    rolling_max = []
    for i in range(len(numbers) + 1):
        # Generate the rolling maximum
        rolling_max.append(numbers[i - 1])
        if i % 30 == 0:
            # Save the rolling maximum found at the end of every 30 elements
            rolling_max_save.append(rolling_max[-1])
            rolling_max = rolling_max[:-1]
        elif i == len(numbers):
            # Save the last rolling maximum
            rolling_max_save.append(numbers[-1])
    # Save the last rolling maximum
    rolling_max_save.append(numbers[-1])
    return rolling_max_save

