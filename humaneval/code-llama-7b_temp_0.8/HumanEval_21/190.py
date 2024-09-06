from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    # check input
    if not numbers or len(numbers) <= 1:
        raise ValueError("Input list must have at least two elements")
    # get min and max values
    min_val = min(numbers)
    max_val = max(numbers)
    # calculate range and ratio
    range_ = max_val - min_val
    if range_ == 0:
        ratio = 1
    else:
        ratio = 1 / range_
    # shift everything up by min_val
    new_numbers = [number + min_val for number in numbers]
    # transform by ratio
    return [new_number * ratio for new_number in new_numbers]

