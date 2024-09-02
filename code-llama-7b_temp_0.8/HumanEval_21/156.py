from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    # list to store results
    rescaled_numbers = []
    # get the minimum and maximum numbers from the list
    min_number, max_number = min(numbers), max(numbers)
    # for each number in the list
    for number in numbers:
        # scale the number and then append the scaled number to the results list
        rescaled_numbers.append((number - min_number) / (max_number - min_number))
    return rescaled_numbers
