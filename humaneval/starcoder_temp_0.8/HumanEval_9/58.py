from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    output = []

    # Start from the left
    for num in numbers:
        if len(output) == 0:
            output.append(num)
        else:
            output.append(max(num, output[-1]))

    return output

