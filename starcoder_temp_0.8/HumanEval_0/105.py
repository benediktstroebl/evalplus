from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    # if there is not at least two elements in list, return false
    if len(numbers) <= 1:
        return False
    # sort the list and iterate through it
    sorted_numbers = sorted(numbers)
    for index in range(len(sorted_numbers)-1):
        if abs(sorted_numbers[index] - sorted_numbers[index+1]) < threshold:
            return True
    return False
