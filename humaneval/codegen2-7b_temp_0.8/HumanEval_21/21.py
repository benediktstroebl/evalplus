from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("numbers must have at least two elements")

    min_num = min(numbers)
    max_num = max(numbers)
    if min_num == max_num:
        return numbers
    elif max_num - min_num < 1e-6:
        return [0.0] * len(numbers)
    else:
        return [(n - min_num) / (max_num - min_num) for n in
