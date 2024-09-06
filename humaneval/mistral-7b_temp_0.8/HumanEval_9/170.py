from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # max_index = 0
    # max_value = numbers[0]
    # rolling_max = []
    # for number in numbers:
    #     if number > max_value:
    #         max_value = number
    #         max_index = rolling_max.index(max_value) + 1 if len(rolling_max) > 0 else 1
    #     rolling_max.append(max_value)
    # return rolling_max

    # from operator import itemgetter
    # return [max(numbers[i:j]) for i, j in enumerate(range(len(numbers)), 1)]

    # rolling_max = [numbers[0]]
    # for number in numbers[1:]:
    #     rolling_max.append(max(rolling_max[-1], number))
    # return rolling_max

    # return [max(numbers[i:j]) for i, j in enumerate(range(len(numbers)), 1)]

    # rolling_max = []
    # for number in numbers:
    
