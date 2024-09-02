from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("Rescaling requires at least two numbers!")

    min_n, max_n = min(numbers), max(numbers)

    if min_n == max_n:
        return [1 for _ in numbers]

    return [(n - min_n) / (max_n - min_n) for n in numbers]

