from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    # if you want to test the sort method
    # numbers.sort()
    # for i in range(len(numbers)-1):
    #    if numbers[i+1] - numbers[i] <= threshold:
    #        return True
    # return False

    #if you want to test the set method
    # return bool(len(set(numbers)) < len(numbers))

    #if you want to test the "not in" operator
    for i in range(len(numbers)-1):
        if abs(numbers[i] - numbers[i+1]) <= threshold:
            return True
    return False
