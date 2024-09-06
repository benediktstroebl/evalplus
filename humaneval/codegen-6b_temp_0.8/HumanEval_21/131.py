from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    i = 0
    for number in numbers:
        if number < 0:
            i += 1
    if i == len(numbers):
        print("Warning: all numbers are negative, answer is not a unit interval")
        return numbers
    else:
        for j in range(i, len(numbers)):
            numbers[j] = (numbers[j] - min(numbers)) / (max(numbers) - min(numbers))
        return numbers

