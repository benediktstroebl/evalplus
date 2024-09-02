from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    min_val = min(numbers)
    max_val = max(numbers)
    
    # check if the list is all same number
    if numbers.count(min_val) == len(numbers) and numbers.count(max_val) == len(numbers):
        return numbers
    
    difference = max_val - min_val
    exponent = 1.0 / difference
    
    return [((val - min_val) * exponent) for val in numbers]

    pass

