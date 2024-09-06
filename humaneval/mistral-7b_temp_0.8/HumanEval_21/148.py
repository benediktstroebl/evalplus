

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    max_number = max(numbers)
    min_number = min(numbers)
    delta = max_number - min_number

    def rescale_to_unit(number):
        return (number - min_number) / delta

    return [rescale_to_unit(number) for number in numbers]

