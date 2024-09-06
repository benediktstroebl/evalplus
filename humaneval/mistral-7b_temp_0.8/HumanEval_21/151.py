from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    # 1. Check that we have at least two elements
    if len(numbers) < 2:
        raise ValueError("not enough elements to rescale")

    # 2. Get the smallest number
    min_value = min(numbers)

    # 3. Get the largest number
    max_value = max(numbers)

    # 4. Get the difference between smallest and largest number
    difference = max_value - min_value

    # 5. Scale each number to the difference between the smallest and largest
    # by subtracting the smallest number and dividing by the difference
    scaled_numbers = [(number - min_value) / difference for number in numbers]

    # 6. Return the scaled list
    return scaled_numbers

