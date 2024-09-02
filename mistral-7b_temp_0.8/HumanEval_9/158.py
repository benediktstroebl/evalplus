from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # your code here
    result = []
    max_numbers = []
    for number in numbers:
        if not max_numbers:
            max_numbers.append(number)
        else:
            if number > max_numbers[-1]:
                max_numbers.append(number)
            elif number == max_numbers[-1]:
                max_numbers.append(number)
            else:
                max_numbers.pop()
                max_numbers.append(number)
        result.append(max_numbers[-1])

    return result

