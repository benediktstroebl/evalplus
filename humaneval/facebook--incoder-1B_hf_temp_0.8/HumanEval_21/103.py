from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    # Note that this implementation assumes that numbers don't contain negative numbers
    min_num, max_num = min(numbers), max(numbers)
    rescaled_numbers = []
    steps = [
        (max_num - min_num) / num,
        0.0,
        0.5 * (max_num - min_num) / (num - 1)
        for num in numbers
    ]

    for num in numbers:
        rescaled_numbers.append(
            (num - min_num) / steps[steps.index(num)] + min_num
        )

    return rescaled_numbers


# noinspection PyTypeChecker