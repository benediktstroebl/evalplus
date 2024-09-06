from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    scaled = [0.0] * (len(numbers) - 1)
    scaled[0] = numbers[0]
    scaled[-1] = 1.0
    for i in range(len(numbers) - 2):
        scaled[i] = (numbers[i + 1] - numbers[i]) / (scaled[i + 1] - scaled[i])
    return scaled

