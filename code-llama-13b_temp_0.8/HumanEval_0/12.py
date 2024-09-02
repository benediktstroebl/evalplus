from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    # we can go through the list and compare each two neighboring elements
    # we can also use the fact that if we know the closest two elements in the list, the closest elements are also the closest
    # among other elements (we can maintain the list of closest two elements)
    # but we have to use the absolute difference to make sure we don't compare elements which are further away than threshold
    # for example for threshold 1, 1.0 and 2.0 are closer than 1.5 and 2.5
    return _has_close_elements_simple(numbers, threshold)
    # return _has_close_elements_optimal(numbers, threshold)

