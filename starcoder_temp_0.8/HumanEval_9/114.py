from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    max_until_now = numbers[0]
    max_so_far = numbers[0]

    output_numbers = [max_until_now]

    for element in numbers[1:]:
        if element > max_until_now:
            max_until_now = element
        elif element < max_until_now:
            max_until_now = max_so_far
        output_numbers.append(max_until_now)
        max_so_far = max(max_so_far, element)

    return output_numbers

