from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError(f"Cannot rescale to unit with less than two numbers: {numbers}")

    first_number = numbers[0]
    last_number = numbers[-1]
    first_number -= first_number
    last_number -= first_number

    numbers_rescaled = [first_number + number * last_number for number in numbers]
    return numbers_rescaled

