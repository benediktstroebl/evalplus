from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if len(numbers) < 2:
        return numbers

    current_max = numbers[0]
    current_numbers = numbers[:]
    for i in range(1, len(current_numbers)):
        if current_numbers[i] > current_max:
            current_max = current_numbers[i]
        else:
            current_numbers[i:i+1] = [current_max]
            current_max = numbers[i]

    return current_numbers

