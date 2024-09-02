from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    results = []
    max_value = numbers[0]
    for number in numbers:
        if number == max_value:
            results.append(number)
        elif number > max_value:
            max_value = number
            results.append(max_value)
    
