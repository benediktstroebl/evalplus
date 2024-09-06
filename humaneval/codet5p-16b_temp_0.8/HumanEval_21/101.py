from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """

    assert len(numbers) >= 2

    minimum = numbers[0]
    maximum = numbers[0]

    for i in numbers:
        if minimum > i:
            minimum = i
        if maximum < i:
            maximum = i

    if maximum == minimum:
        new_numbers = [0.0] * len(numbers)
        return new_numbers
    else:
        scale = 1.0 / (maximum - minimum)
        for i in range(len(numbers)):
            numbers[i] = scale * (numbers[i] - minimum)
        return numbers
