from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """

    # check that there are at least 2 elements
    if len(numbers) <= 1:
        raise ValueError('Number of elements must be at least 2')

    # check that numbers are all of the same type
    if not all(isinstance(x, type(numbers[0])) for x in numbers[1:]):
        raise TypeError('All numbers must be of the same type')

    # check that numbers are not all the same
    if numbers[0] == numbers[-1]:
        raise ValueError('Numbers must not be all the same')

    # find the smallest number
    smallest = min(numbers)

    # find the difference between the smallest and largest
    diff = numbers[-1] - smallest

    # rescale all numbers by dividing the difference
    return [((x - smallest) / diff) for x in numbers]

