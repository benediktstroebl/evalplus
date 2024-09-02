from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    rescale_factor = 1.0 / (max(numbers) - min(numbers))
    scale_function = lambda x: rescale_factor * (x - min(numbers))

    return [scale_function(x) for x in numbers]
