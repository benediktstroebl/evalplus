from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    node = 0
    previous_max = numbers[0]
    max_nodes = [numbers[0]]
    while node < len(numbers):
        if previous_max < numbers[node]:
            max_nodes.append(numbers[node])
            previous_max = numbers[node]
        node += 1

    return max_nodes

