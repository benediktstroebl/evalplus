from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        return numbers

    # Convert to absolute values
    abs_numbers = [abs(number) for number in numbers]
    # Convert to relative values
    rel_numbers = [(number - min(abs_numbers)) / max(abs_numbers) for number in abs_numbers]
    # Apply linear transform
    return [x * rel_number for x in numbers]

