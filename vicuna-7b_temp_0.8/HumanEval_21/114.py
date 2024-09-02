from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    min_val = min(numbers)
    max_val = max(numbers)
    num_vals = len(numbers)
    scale_vals = [1.0 / (max_val - min_val), 1.0 / (num_vals - 1)]
    scaled_numbers = [min_val + (val - min_val) * scale_vals[i] for i, val in enumerate(numbers)]
    return [val for i, val in enumerate(scaled_numbers) if val != 0.0]

