from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    # Check if the list is empty or if it has a single element
    # If so, raise an exception
    if len(numbers) == 0:
        raise IndexError
    if len(numbers) == 1:
        raise ValueError

    # Perform the rescaling to 0 and 1
    min_num = min(numbers)
    max_num = max(numbers)
    return [(float(i) - min_num) / (max_num - min_num) for i in numbers]
