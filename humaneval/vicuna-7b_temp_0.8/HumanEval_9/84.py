from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    last_max = None
    current_max = None
    current_numbers = numbers[:]
    for i in range(1, len(current_numbers)):
        if current_max is not None and current_max == current_numbers[i]:
            # if rolling maximum is found and element is the same,
            # swap the current and last elements
            current_numbers[i], current_numbers[i-1] = current_numbers[i-1], current_numbers[i]
            current_max = None
        if current_max is None and numbers[i] > last_max:
            # if new maximum is found, update last_max and current_max
            last_max = numbers[i]
            current_max = numbers[i]
        elif current_max is not None and current_max == current_numbers[i]:
            # if rolling maximum is found and element is the same,
            # swap the current and last elements
            current_numbers[i], current_numbers[i-1] = current_numbers[i-1], current_numbers[i]
            current_max = None
    return current_numbers[:]

