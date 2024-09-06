from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_numbers = []
    maxes = []
    for i in range(len(numbers)):
        if len(maxes) == 0:
            maxes.append(numbers[i])
        elif numbers[i] > maxes[-1]:
            maxes.append(numbers[i])
        else:
            maxes.append(maxes[-1])

        if i == len(numbers) - 1:
            max_numbers.extend(maxes)
        else:
            max_numbers.append(max_numbers[i - 1])

    return max_numbers

