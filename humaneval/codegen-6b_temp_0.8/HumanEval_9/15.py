from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_list = []
    for i in range(0, len(numbers)):
        # make an initial slice of list
        start_slice = numbers[0:i+1]
        # make an other slice of list
        end_slice = numbers[i+1:len(numbers)]
        # start_slice + max(end_slice) is the local max
        max_list.append(max(start_slice + end_slice))
    return max_list

