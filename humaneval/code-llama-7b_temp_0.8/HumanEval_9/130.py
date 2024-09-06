from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # Your code goes here
    if len(numbers) == 0:
        return []

    result: List[int] = []
    current_max = numbers[0]
    for number in numbers:
        if number > current_max:
            current_max = number
        result.append(current_max)

    return result

