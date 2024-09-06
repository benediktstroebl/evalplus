from typing import List
def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given a list of numbers (at least two elements), apply a linear transform to that list,
        such that the smallest number will become 0 and the largest will become 1 """

    # ensure the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("List must have at least two elements")

    # sort the list and get the index of the smallest and largest number
    numbers.sort()
    idx_smallest = len(numbers) - 1
    idx_largest = 0

    rescaled_numbers = []
    for idx, number in enumerate(numbers):
        prop = (number - numbers[idx_largest]) / (numbers[idx_smallest] - numbers[idx_largest])
        rescaled_numbers.append(prop)

    return rescaled_numbers
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]