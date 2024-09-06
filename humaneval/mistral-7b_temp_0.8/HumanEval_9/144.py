from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    assert all(isinstance(n, int) for n in numbers), "input should be a list of integers"
    max_indexes = [0]
    max_values = [numbers[0]]
    for i in range(1, len(numbers)):
        if numbers[i] > max_values[-1]:
            max_indexes.append(i)
            max_values.append(numbers[i])
        else:
            index_to_swap = max_indexes[-1]
            max_indexes[-1] = i
            max_indexes.insert(index_to_swap, max_indexes.pop(index_to_swap))
            max_values[-1] = max_values[index_to_swap]
            max_values[index_to_swap] = numbers[i]
    return max_values

