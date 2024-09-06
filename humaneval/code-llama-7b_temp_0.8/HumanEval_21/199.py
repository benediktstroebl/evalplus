from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    # check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("The list must have at least two elements")
    # check if the list contains only numbers
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise TypeError("The list must contain only numbers")
    # check if the list contains only numbers
    if not all(x >= 0 for x in numbers):
        raise ValueError("The list must contain only positive numbers")
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise TypeError("The list must contain only numbers")

    rescaled_numbers = list()
    smallest_number = min(numbers)
    largest_number = max(numbers)
    for number in numbers:
        if largest_number == smallest_number:
            rescaled_numbers.append(0.0)
        else:
            rescaled_number = (number - smallest_number) / (largest_number - smallest_number)
            rescaled_numbers.append(rescaled_number)
    return rescaled_numbers

