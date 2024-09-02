from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """

    # Find the smallest number
    min_number = min(numbers)

    # Find the largest number
    max_number = max(numbers)

    # Find the difference between the smallest and largest
    diff = max_number - min_number

    # Find the difference between each number and the smallest number
    diff_from_min = [i - min_number for i in numbers]

    # Divide each difference from the smallest number by the difference between largest and smallest
    # (This is the new "unit" we want)
    return [i / diff for i in diff_from_min]

