from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    # MIN_VAL is the minimum value of the rescaled array
    MIN_VAL = 0
    # MAX_VAL is the maximum value of the rescaled array
    MAX_VAL = 1
    # DIFFERENCE is the difference between the largest number and the smallest number
    DIFFERENCE = (
        max(numbers) - min(numbers)
    )  # max() and min() are Python builtins that return the largest/smallest elements in a list

    # We use a list comprehension to build a new list by applying the following equation to every number
    # (x - smallest number) * (1 - 0) / (largest number - smallest number) + 0
    return [
        ((num - min(numbers)) * (MAX_VAL - MIN_VAL)) / DIFFERENCE + MIN_VAL
        for num in numbers
    ]

