from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    if len(numbers) < 2:
        return numbers
    
    n = len(numbers)
    current_max = numbers[0]
    current_numbers = numbers[:n]
    max_list = [current_max]
    
    for i in range(1, n):
        if current_numbers[i] > current_max:
            current_max = current_numbers[i]
            max_list[-1] = current_max
        current_numbers[i:i+2] = [numbers[i], numbers[i+1]]
        max_list.extend(current_numbers[:i+1])
    
    return max_list[1:-1]

