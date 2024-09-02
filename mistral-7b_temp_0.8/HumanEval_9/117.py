from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    # check if numbers is an instance of list
    if not isinstance(numbers, list):
        raise ValueError(f"'numbers' parameter must be an instance of 'list' instead of '{type(numbers)}'")

    # check if all elements of numbers are instance of int
    for number in numbers:
        if not isinstance(number, int):
            raise TypeError(f"'numbers' list must contain int elements, instead found: '{type(number)}'")

    # check if numbers is an empty list
    if len(numbers) == 0:
        raise ValueError("'numbers' list must contain at least one element")

    # check if the given numbers are sorted
    if numbers[0] > numbers[1]:
        raise ValueError("'numbers' list must be sorted")

    # generate list of rolling maximum element found until given moment in the sequence
    max_of_list = [numbers[0]]
    for i in range(1, len(numbers)):
        if numbers[i] > max_of_list[-1]:
            max_of_list
