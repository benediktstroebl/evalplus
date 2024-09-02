from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    result: List[int] = []
    index: int = len(numbers) - 1
    for number in numbers:
        if number >= numbers[index]:
            index -= 1
            result.append(number)
        else:
            result.append(numbers[index])
    return
