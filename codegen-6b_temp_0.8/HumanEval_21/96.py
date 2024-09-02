from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    # find min and max
    max_num = max(numbers)
    min_num = min(numbers)
    # create function that returns 1 if input >= min and 0 if input < min
    transform_min = lambda num: 1 if num >= min_num else 0
    # apply function to each element
    transformed_nums = [transform_min(num) for num in numbers]
    # return final list
    return transformed_nums

