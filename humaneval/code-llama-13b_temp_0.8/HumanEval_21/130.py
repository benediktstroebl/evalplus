from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    # if len(numbers) == 0:
    #     return []
    # else:
    #     min_number = min(numbers)
    #     max_number = max(numbers)
    #     difference = max_number - min_number
    #     return [(num-min_number)/difference for num in numbers]

    # similar to below, but no need to check for empty array
    # shorter and more efficient
    min_num = min(numbers)
    difference = max(numbers) - min_num
    return [(num-min_num)/difference for num in numbers]

