from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    result = []
    # find last index we can see maximum element from
    maximum = max(numbers)
    index_maximum = numbers.index(maximum)
    # we can see maximum element from every index from previous to current.
    # Every time we add new element in result, we have to keep the maximum element
    # at the end of result array
    for index, number in enumerate(numbers):
        if index == 0:
            result.append(number)
        else:
            if number > max(result):
                result.append(number)
            else:
                result.append(result[-1])
    return result

