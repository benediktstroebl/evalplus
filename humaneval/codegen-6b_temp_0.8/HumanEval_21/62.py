from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    numbers_rescaled = []
    max_number = max(numbers)
    min_number = min(numbers)
    count = 0
    for i in numbers:
        if i > max_number:
            numbers_rescaled.append(0)
            count += 1
        elif i < min_number:
            numbers_rescaled.append(1)
            count += 1
        else:
            numbers_rescaled.append((i - min_number) / (max_number - min_number))
    return numbers_rescaled

