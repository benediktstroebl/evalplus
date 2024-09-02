from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """

    # find the minimum and maximum numbers in the list
    min_number = min(numbers)
    max_number = max(numbers)

    # find the difference between the maximum and the minimum
    difference = max_number - min_number

    # create a list of rescaled numbers
    rescaled_numbers = []

    # iterate through the list of numbers
    for number in numbers:
        # find the difference between the number and the minimum
        difference_from_min = number - min_number

        # find the number's rescaled value
        rescaled_value = difference_from_min / difference

        # append the rescaled number to the list of rescaled numbers
        rescaled_numbers.append(rescaled_value)

    # return the list of rescaled numbers
    return rescaled_numbers


