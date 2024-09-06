from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    numbers = list(numbers)
    max_sum = numbers[0]
    result = [numbers[0]]

    for i in range(1, len(numbers)):
        if max_sum > numbers[i]:
            max_sum = max_sum
        else:
            max_sum = numbers[i]

        result.append(max_sum)

    return result

