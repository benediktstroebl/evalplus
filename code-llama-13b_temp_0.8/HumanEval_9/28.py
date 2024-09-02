from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # assert len(numbers) > 0, "Empty lists are not supported"
    # maximum = numbers[0]
    # result = [maximum]
    # for i in range(1, len(numbers)):
    #     maximum = max(maximum, numbers[i])
    #     result.append(maximum)
    # return result
    maximum = numbers[0]
    return [maximum] + [
        max(maximum, value) for value in numbers[1:]
    ]

