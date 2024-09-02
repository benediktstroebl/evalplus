from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    # compute the range of the input list
    max_number = max(numbers)
    min_number = min(numbers)
    range_of_numbers = max_number - min_number

    # now compute the slope and intercept for the equation y = mx + b, where m is the
    # slope of the transformed list, and b is the intercept (that is, the y-intercept)
    slope = range_of_numbers / (max_number - min_number)
    y_intercept = min_number - (max_number * slope)

    # finally, loop through the input list and transform each number by multiplying by slope
    # and adding the intercept
    transformed_numbers = []
    for number in numbers:
        transformed_numbers.append((number - min_number) * slope + y_intercept)

    return transformed_numbers

