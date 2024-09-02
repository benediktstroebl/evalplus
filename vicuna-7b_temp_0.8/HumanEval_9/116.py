from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    current_max = numbers[0]
    current_index = 0
    numbers_list = [current_max] + numbers[1:]

    for i in range(1, len(numbers_list)):
        if numbers_list[i] > numbers_list[i-1]:
            current_max = numbers_list[i]
            current_index = i

        numbers_list[i:i+1] = [numbers_list[j] for j in range(current_index, len(numbers_list))]

    return numbers_list[:]

