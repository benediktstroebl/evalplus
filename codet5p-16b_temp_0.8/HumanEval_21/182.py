from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """

    min_number = numbers[0]
    max_number = numbers[0]
    for num in numbers:
        if min_number > num:
            min_number = num
        if max_number < num:
            max_number = num

    difference = max_number - min_number
    scaling_factor = 1 / difference
    new_numbers = []
    for num in numbers:
        new_num = scaling_factor * (num - min_number)
        new_numbers.append(new_num)

    return new_numbers
