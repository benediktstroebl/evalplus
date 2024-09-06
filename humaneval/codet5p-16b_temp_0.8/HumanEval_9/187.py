from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    numbers_size = len(numbers)
    rolling_max_list = []
    for i in range(numbers_size):
        max_index = i
        for j in range(i + 1, numbers_size):
            if numbers[j] > numbers[max_index]:
                max_index = j
        if max_index!= i:
            numbers[i], numbers[max_index] = numbers[max_index], numbers[i]

        rolling_max_list.append(numbers[i])
    return rolling_max_list

