from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """

    # find max
    max_val = max(numbers)
    # find min
    min_val = min(numbers)

    # subtract the min from the list
    new_list = list(x - min_val for x in numbers)

    # divide the new list by the max
    new_list = list(x / max_val for x in new_list)

    return new_list

