from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """

    # checking that the list has at least two elements
    if len(numbers) < 2:
        raise ValueError('You cannot rescale a list with only one element')

    # getting the min and the max values
    min_value = min(numbers)
    max_value = max(numbers)

    # handling the case where min == max
    if min_value == max_value:
        return [0.0 for i in numbers]

    # return the list of the transformed numbers
    return [(number - min_value) / (max_value - min_value) for number in numbers]
