from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    numbers_sorted = sorted(numbers)
    min_index = 0
    max_index = len(numbers_sorted) - 1
    for i in range(1, len(numbers_sorted)):
        if numbers_sorted[i] < numbers_sorted[min_index]:
            min_index = i
        if numbers_sorted[i] > numbers_sorted[max_index]:
            max_index = i
    min_number = numbers_sorted[min_index]
    max_number = numbers_sorted[max_index]
    scale_factor = (max_number - min_number) / 2
    scaled_numbers = [min_number * (number - min_number) / (max_number - min_number) + min_number for number in numbers]
    return [scaled_number / scale_factor for scaled_number in scaled_numbers]