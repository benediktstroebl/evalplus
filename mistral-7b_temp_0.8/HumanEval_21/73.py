from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    # check if length of numbers is larger than one
    if len(numbers) == 1:
        return numbers

    # compute maximum and minimum value
    maximum = max(numbers)
    minimum = min(numbers)

    # compute ratio and apply to the list
    ratio = (maximum - minimum)
    for i in range(len(numbers)):
        numbers[i] = (numbers[i] - minimum) / ratio

    return numbers
