from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    assert len(numbers) >= 2
    min_val = min(numbers)
    max_val = max(numbers)
    min_val_index = numbers.index(min_val)
    max_val_index = numbers.index(max_val)
    rescale_factor = 1 / (max_val - min_val)
    numbers[min_val_index] = 0
    numbers[max_val_index] = 1
    for i in range(len(numbers)):
        numbers[i] = numbers[i] * rescale_factor

    return numbers

