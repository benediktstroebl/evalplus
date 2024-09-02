from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("the input list must contain at least two elements")

    # step 1: find the max and the min of the list
    max_number = max(numbers)
    min_number = min(numbers)

    # step 2: compute the delta and the scale
    delta = max_number - min_number
    if delta == 0:
        scale = 1
    else:
        scale = 1 / delta

    # step 3: apply the scale to each number in the list
    res = [scale * (n - min_number) for n in numbers]

    return res
