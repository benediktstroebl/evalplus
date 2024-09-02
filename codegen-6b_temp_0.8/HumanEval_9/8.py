from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    result = [None for _ in range(len(numbers))]
    scores = [None for _ in range(len(numbers))]

    # scores[i]: max number at the moment at position i
    # result[i]: max number till the moment of position i
    scores[0] = numbers[0]
    result[0] = numbers[0]
    for i in range(1, len(numbers)):
        scores[i] = max(numbers[i], scores[i-1])
        result[i] = max(numbers[i], result[i-1])

    return result

