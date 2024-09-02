from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # sort numbers in place to get lowest to highest and smallest to biggest
    numbers.sort()
    # set lower and upper bounds to first two
    lower_bound = numbers[0]
    upper_bound = numbers[1]
    # get rid of the first two
    numbers = numbers[2:]
    # iterate over remaining numbers
    for number in numbers:
        # if current is lower, set lower bound
        if number < lower_bound:
            lower_bound = number
        # if current is higher, set upper bound
        if number > upper_bound:
            upper_bound = number
    # return lower bound, upper bound
    return lower_bound, upper_bound
