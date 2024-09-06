from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    smallest = float('inf')
    largest = float('-inf')

    for number in numbers:
        smallest = min(smallest, number)
        largest = max(largest, number)

    a = 1.0 / (largest - smallest)
    b = - smallest * a

    # inline multiply
    return [a * number + b for number in numbers]

