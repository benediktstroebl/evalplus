from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    assert len(numbers) > 0, "You should enter a non-empty list of integers."

    result = []
    max_value = numbers[0]
    for i in range(1, len(numbers) + 1):
        if numbers[i - 1] < numbers[i - 2]:
            max_value = numbers[i - 1]
        else:
            max_value = numbers[i - 2]
        result.append(max_value)

    return result

