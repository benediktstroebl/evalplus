from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    # put all the numbers into a set
    numbers_set = set(numbers)

    # for each number, check if there is another number in the set that is closer than the threshold
    for number in numbers_set:
        # if there is, return true
        if len(numbers_set - set(filter(lambda x: abs(x - number) <= threshold, numbers_set))) > 0:
            return True

    # if not, return false
    return False

