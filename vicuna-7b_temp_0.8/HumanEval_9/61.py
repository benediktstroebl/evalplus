from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    n = len(numbers)
    result = [numbers[i:i+1] for i in range(0, n, 1)]
    current_max = max(result[0])
    max_found = 1
    for i in range(1, n):
        for j in range(i-1, -1, -1):
            if numbers[j] > current_max:
                current_max = numbers[j]
                max_found += 1
                result[i-1] = numbers[j-max_found]
        else:
            result[i-1] = current_max
            max_found += 1
    return result[1:]

