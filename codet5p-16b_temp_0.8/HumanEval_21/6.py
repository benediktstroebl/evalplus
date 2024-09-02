from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """

    sorted_numbers = sorted(numbers)
    max_number = sorted_numbers[-1]
    min_number = sorted_numbers[0]
    
    unit_numbers = []
    for number in numbers:
        unit_numbers.append((number - min_number) / (max_number - min_number))
    
    return unit_numbers

