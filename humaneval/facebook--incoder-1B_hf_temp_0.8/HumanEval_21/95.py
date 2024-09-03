from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    assert len(numbers) > 0
    minimum = numbers[0]
    maximum = numbers[-1]

    # Ensure that numbers are within the given range
    min_range = max(minimum, minimum)
    max_range = min(maximum, maximum)
    assert min_range <= max_range, "{} <= {}".format(minimum, max_range)
    rescale = [float(number) / float(max_range) for number in numbers]

    # Ensure that rescaled numbers are within the given range
    min_range = max(rescale[0], rescale[0])
    max_range = min(rescale[-1], rescale[-1])
    assert min_range <= max_range, "{} <= {}".format(rescale[0], rescale[-1])

    return rescale

