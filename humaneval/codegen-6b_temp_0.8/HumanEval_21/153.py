from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError('rescale_to_unit: passed an array with fewer than two elements')

    min_num = min(numbers)
    max_num = max(numbers)
    min_index = numbers.index(min_num)
    max_index = numbers.index(max_num)

    if min_index > max_index:
        min_index, max_index = max_index, min_index

    return [(max_num - i) / (max_num - min_num) for i in numbers[min_index:max_index + 1]]

