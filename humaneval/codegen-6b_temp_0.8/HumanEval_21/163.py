from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    # If there are only two numbers, we're done
    if len(numbers) == 2:
        return [n / max(numbers) for n in numbers]

    # Find the smallest and largest values
    min_v, max_v = min(numbers), max(numbers)

    # Perform the rescaling
    return [n / max_v for n in numbers]

