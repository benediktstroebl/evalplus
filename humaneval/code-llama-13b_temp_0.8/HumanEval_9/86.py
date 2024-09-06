from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # store the max value found so far and its index
    max_num: Tuple[int, int] = (float("-inf"), 0)
    res: List[int] = []

    for i, num in enumerate(numbers):
        # if the given value is higher than the max value
        # found so far, update the max value
        if num > max_num[0]:
            max_num = num, i
        # append the max value to the result
        res.append(max_num[0])

    # if a max value is not found, return a list of zeros
    if not max_num[0]:
        return [0] * len(numbers)

    # update the list of results to include
    # a sequence of max values at the beginning
    # if the first element in the list is not max
    if max_num[1] != 0:
        res[: max_num[1] + 1] = [max_num[0]] * (max_num[1] + 1)

    return res

