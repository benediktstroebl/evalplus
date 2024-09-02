from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """

    if len(numbers) < 2:
        raise Exception("too few items in list to rescale")

    # create the list that will contain the rescaled numbers
    rescaled = []

    # find the min and max values in the list
    min_val = min(numbers)
    max_val = max(numbers)

    # transform the list by rescaling it so that the minimum value is 0 and the maximum is 1
    for value in numbers:
        rescaled.append((value - min_val) / (max_val - min_val))

    return rescaled
