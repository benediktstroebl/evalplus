from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    result = []
    temp = []
    for i in range(len(numbers)):
        if not temp:
            temp.append(numbers[i])
        elif numbers[i] > max(temp):
            temp.append(numbers[i])
        else:
            temp.pop(0)
            temp.append(numbers[i])
        # temp = temp[-n:]
        # temp.append(numbers[i])
        result.append(max(temp))
    return result

