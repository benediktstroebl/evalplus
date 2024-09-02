from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    moments = [None] * 11
    for i in range(len(numbers)):
        if moments[i] is not None:
            # Return previous maximum element
            if numbers[i] >= moments[i]:
                return [numbers[i-1]] + moments[i-1:]
            else:
                moments[i] = None  # Mark moment as invalid
        else:
            moments[i] = numbers[i]
    return [numbers[-1]] + moments[:]

