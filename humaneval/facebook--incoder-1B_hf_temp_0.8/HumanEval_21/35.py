from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    minimum = numbers[0]
    maximum = numbers[-1]

    # First we find the difference between each number in the list
    differences = [abs(x - minimum) for x in numbers]

    # Now we find how many times each number has been rescaled
    rescaled = [int(x * 1000) / maximum for x in differences]

    # Now we convert the rescaled numbers to their proper units
    return [x / y for x, y in zip(rescaled, differences)]

