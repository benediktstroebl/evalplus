from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    # Assign values to a list
    output: List[int] = [numbers[0]]

    # Run the rolling maximum algorithm
    for index in range(1, len(numbers)):
        output.append(max(numbers[index], output[index - 1]))

    return output

