from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    min_val = min(numbers)
    max_val = max(numbers)
    min_index = numbers.index(min_val)
    max_index = numbers.index(max_val)
    rescaled = []
    for i in range(len(numbers)):
        rescaled.append(float((numbers[i] - min_val) / float(max_val - min_val)))
    rescaled[min_index] = 0
    rescaled[max_index] = 1
    return rescaled


