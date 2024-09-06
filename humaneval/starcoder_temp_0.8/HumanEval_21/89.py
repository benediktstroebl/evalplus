from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    assert len(numbers) >= 2, "Need at least 2 numbers to rescale"
    min_val = min(numbers)
    max_val = max(numbers)
    if min_val == max_val:
        return [0.0] * len(numbers)
    scaled = []
    for num in numbers:
        scaled.append((num - min_val) / (max_val - min_val))
    return scaled
