from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    result = [max(numbers[0], numbers[1])]
    max_value = result[0]

    for index in range(2, len(numbers)):
        if numbers[index - 1] > max_value:
            max_value = numbers[index - 1]
        elif numbers[index - 2] > max_value:
            max_value = numbers[index - 2]

        result.append(max_value)

    return result

