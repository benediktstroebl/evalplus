from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    max_number = max(numbers)
    min_number = min(numbers)
    rescaled_numbers = []

    if (max_number - min_number) != 0:
        for n in numbers:
            rescaled_numbers.append((n - min_number) / (max_number - min_number))
        return rescaled_numbers
    elif max_number != 0:
        return [n / max_number for n in numbers]
    else:
        return [n for n in numbers]

