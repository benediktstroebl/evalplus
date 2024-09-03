from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError(
            "rescale_to_unit was called with a list of less than two elements, but received {}".format(
                numbers))

    min_, max_ = numbers[0], numbers[0]
    for n in numbers[1:]:
        if n < min_:
            min_ = n
        if n > max_:
            max_ = n

    return [(n - min_) / (max_ - min_) for n in numbers]

