from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_elem = -1
    max_elem_count = 0
    max_elem_index = 0
    result = []
    for i in range(len(numbers)):
        if max_elem < numbers[i]:
            result.append(max_elem)
            max_elem_count = 0
            max_elem = numbers[i]
            max_elem_index = i
        else:
            max_elem_count += 1
            if max_elem_count > max_elem_index:
                max_elem_index = max_elem_count
    result.append(max_elem)
    return result

