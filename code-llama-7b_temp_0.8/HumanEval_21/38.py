from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    # STEP 1: check that the numbers are different
    if len(set(numbers)) == 1:
        raise ValueError("all numbers in the list are equal")

    # STEP 2: compute the minimum and maximum
    min_num = min(numbers)
    max_num = max(numbers)

    # STEP 3: calculate the scale factor
    scale_factor = max_num - min_num

    # STEP 4: calculate the offset
    offset = min_num

    # STEP 5: return the scaled numbers
    return [
        (n - offset) / scale_factor
        for n in numbers
    ]
