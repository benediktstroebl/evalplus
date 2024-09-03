from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    assert numbers[0] == 0 and numbers[-1] == 1
    rescaled = []
    for i in range(len(numbers) - 1):
        if numbers[i] <= numbers[i+1]:
            rescaled.append(numbers[i] / (numbers[i+1] - numbers[i]))
        else:
            rescaled.append(1)
    rescaled.append(0)
    return rescaled

