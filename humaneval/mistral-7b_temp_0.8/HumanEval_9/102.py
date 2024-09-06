from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # create a new list, which will contain rolling max values
    max_seq = []
    # 1. go through the list one element at a time
    for i in range(len(numbers)):
        # 2. get max element in the slice that starts from first element and ends on current element
        max_seq.append(max(numbers[0:i + 1]))
    return max_seq

