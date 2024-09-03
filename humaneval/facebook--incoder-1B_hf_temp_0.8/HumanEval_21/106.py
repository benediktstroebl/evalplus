from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) == 0 or len(numbers) == 1 or len(numbers) == 2:
        return numbers
    if len(numbers) == 1:
        return numbers * 1.0

    min = min(numbers)
    max = max(numbers)
    scale_factor = max - min

    # Find scaling factor
    for number in numbers:
        if number > max:
            scale_factor *= (number - max) / max

    # Apply linear transformation
    return [scale_factor * numbers[i] for i in range(len(numbers))]

