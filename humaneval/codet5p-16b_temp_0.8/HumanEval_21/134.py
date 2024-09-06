from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """

    num_values = len(numbers)
    if num_values == 0:
        return numbers
    elif num_values == 1:
        return [0]

    numbers = sorted(numbers)
    smallest_value = numbers[0]
    largest_value = numbers[num_values - 1]

    transformed_values = []

    for number in numbers:
        transformed_value = (number - smallest_value) / (largest_value - smallest_value)
        transformed_values.append(transformed_value)

    return transformed_values

