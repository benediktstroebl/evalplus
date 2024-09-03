from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    numbers = sorted(numbers)
    min_val = numbers[0]
    max_val = numbers[-1]
    rescale = [min_val]
    for i in range(len(numbers) - 1):
        rescale.append(numbers[i] - rescale[-1])
        rescale[-1] = (numbers[i + 1] - rescale[-1]) / (max_val - min_val)
    return rescale

