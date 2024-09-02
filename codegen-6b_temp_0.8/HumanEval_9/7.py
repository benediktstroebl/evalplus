from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_n = max(numbers)
    ans = []
    for i in range(max_n, -1, -1):
        if i in numbers:
            ans.append(i)
            for j in range(1, len(numbers)):
                if numbers[j] > numbers[j - 1]:
                    numbers[j] = numbers[j - 1]
    return ans

