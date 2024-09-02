from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # TODO: write the function
    # (1) initialize a max_ so far, and a list result.
    max_ = -99999
    result = [1]
    # (2) loop through the list, and compare each number with the current max_
    for number in numbers:
        if number > max_:
            max_ = number
            result.append(max_)
        else:
            result.append(max_)
    return result
