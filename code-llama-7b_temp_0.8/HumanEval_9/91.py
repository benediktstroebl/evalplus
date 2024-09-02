from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # The idea is to generate a new list of numbers with the rolling maximum value for each element
    # To do that, we have to keep track of two things:
    #   - the current rolling maximum value
    #   - the index of the last element that we used to update the rolling maximum value
    rolling_max_list: List[int] = []

    current_max = numbers[0]
    last_index = 0

    for i in range(len(numbers)):
        if numbers[i] > current_max:
            current_max = numbers[i]
            last_index = i

        rolling_max_list.append(current_max)

    # We need to update the last elements of the rolling_max_list so they are correct.
    # To do that, we just need to check that the last element is greater than the
    # previous one and update it if needed.
    for i in range(last_index, len(numbers) - 1, 1):
        if numbers[i] > numbers[i + 1]:
            rolling_max_list[i] = numbers[i]
        else:
            rolling_max_list[i] = numbers[i + 1]

    return rolling_max_list

