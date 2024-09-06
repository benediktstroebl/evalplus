from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    moments = [0] * 10  # 10 moments in the sequence
    result = [None] * 10  # result of the rolling max calculation

    for i in range(len(numbers) - 1):
        if i == 0 or numbers[i] > numbers[i + 1]:
            moments[0] = numbers[i]
            result[0] = moments[0]

        for j in range(1, len(moments)):
            if moments[j - 1] <= moments[j]:
                moments[j] = numbers[i + j]
                result[j] = moments[j]

    return result

