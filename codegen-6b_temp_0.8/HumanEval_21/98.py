from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    smallest_number = float("inf")
    largest_number = float("-inf")
    for number in numbers:
        if number < smallest_number:
            smallest_number = number
        if number > largest_number:
            largest_number = number
    def scale_function(number):
        return 1.0*(number - smallest_number)/(largest_number - smallest_number)
    return list(map(scale_function, numbers))

