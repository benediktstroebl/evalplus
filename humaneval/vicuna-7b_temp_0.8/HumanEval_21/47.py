from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    smallest = min(numbers)
    largest = max(numbers)
    numbers_sorted = sorted(numbers)
    number_of_elements = len(numbers)

    scaled_numbers = [0.0] * number_of_elements
    scaled_numbers[0] = smallest
    scaled_numbers[number_of_elements - 1] = largest

    for i in range(1, number_of_elements - 1):
        scaled_numbers[i] = numbers_sorted[i] * (largest - smallest) / (largest - numbers_sorted[number_of_elements - 1])

    return scaled_numbers

