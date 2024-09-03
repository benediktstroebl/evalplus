from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        return [1.0]
    smallest = numbers[0]
    largest = numbers[-1]
    scalings = []
    for number in numbers:
        if number == 0:
            scalings.append(1.0)
        else:
            scalings.append(1.0 / number)
    scalings.insert(0, 0.0)
    scalings.insert(0, 1.0)
    return scalings + [largest] * (len(numbers) - 1) + [smallest] * (len(numbers) - 1)

