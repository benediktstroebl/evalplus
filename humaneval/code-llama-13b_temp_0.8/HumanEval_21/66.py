from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    pass
    # assert 1 <= len(numbers) <= 5, "List must have between 1 and 5 elements"
    #
    # min_number = min(numbers)
    # max_number = max(numbers)
    # result = []
    #
    # for number in numbers:
    #     new_number = (number - min_number) / (max_number - min_number)
    #     result.append(new_number)
    #
    # return result

    return [(n - min(numbers)) / (max(numbers) - min(numbers)) for n in numbers]

