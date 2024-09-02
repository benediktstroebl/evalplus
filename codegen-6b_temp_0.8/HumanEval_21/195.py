from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    # Hint: you can make this happen in one line with a single line of code.
    # Just make sure it works in this simple version of the function
    min_num = min(numbers)
    rescale_factor = (max(numbers) - min_num) / (1 - min_num)
    return [rescale_factor * (i - min_num) for i in numbers]

