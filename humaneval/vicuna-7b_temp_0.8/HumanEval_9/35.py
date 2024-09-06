from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_values = [max(numbers) for _ in range(len(numbers) - 1)]
    current_max = max_values[-1]
    current_numbers = numbers[:]
    for i in range(len(max_values)):
        numbers[:] = current_numbers
        for j in range(len(current_numbers) - 1):
            if current_numbers[j] > current_max:
                current_max = current_numbers[j]
        numbers[:] = current_numbers
    return current_max

