from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    # Get the minimum number from the given list
    min_number = min(numbers)
    # Get the maximum number from the given list
    max_number = max(numbers)
    # If the minimum number is 0, then we are done
    if min_number == 0:
        return numbers
    # Get the difference between the max and min
    denominator = max_number - min_number
    # If the denominator is 0 (the list is the same number), then we are done
    if denominator == 0:
        return numbers
    # Return the difference between the max and the min divided by the difference
    return [((number - min_number) / denominator) for number in numbers]
