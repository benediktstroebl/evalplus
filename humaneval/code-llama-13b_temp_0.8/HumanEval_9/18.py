from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    previous_max, maximum = None, None
    maximum_list = []
    for number in numbers:
        if previous_max is None:
            maximum = number
        elif number > previous_max:
            maximum = number

        maximum_list.append(maximum)
        previous_max = maximum

    return maximum_list

