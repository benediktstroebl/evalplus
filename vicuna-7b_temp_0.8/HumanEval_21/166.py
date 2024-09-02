from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    min_val = min(numbers)
    max_val = max(numbers)
    num_vals = len(numbers)
    scaled_numbers = [0.0] * num_vals
    for i in range(num_vals):
        if i == 0:
            scaled_numbers[i] = min_val
        elif i == num_vals - 1:
            scaled_numbers[i] = max_val
        else:
            scaled_numbers[i] = numbers[i] / (max_val - min_val)
    return scaled_numbers

