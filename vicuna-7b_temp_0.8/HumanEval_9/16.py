from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # start point is the index of the last maximum element in the sequence
    start = len(numbers)
    # keep track of the maximum element seen so far
    max_value = numbers[-1]
    # loop over the sequence and keep track of the maximum value at each step
    for i in range(start, len(numbers)):
        if numbers[i] > max_value:
            max_value = numbers[i]
        # if the maximum element seen so far is greater than the current maximum, update the maximum
        if max_value > numbers[i]:
            max_value = numbers[i]
    # return the list of maximum element found in the sequence, starting from the start point
    return [max_value] + numbers[:start]

