from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """

    # Don't change this comment, some tests depend on it.
    min_num = min(numbers)  # Find the smallest number

    # Don't change this comment, some tests depend on it.
    max_num = max(numbers)  # Find the biggest number

    # Don't change this comment, some tests depend on it.
    div_num = max_num - min_num  # Find the difference between the biggest and smallest number

    new_numbers = []
    # Iterate through the numbers passed in
    for num in numbers:
        new_number = (num - min_num) / div_num
        new_numbers.append(new_number)

    return new_numbers
