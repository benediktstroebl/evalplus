from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    # to handle empty lists:
    if len(numbers) < 2:
        return numbers

    # using index 0 and 1, and sorting them, we can find the greatest and smallest numbers
    # and their corresponding indices in the list
    greatest_number_index = numbers.index(max(numbers))
    smallest_number_index = numbers.index(min(numbers))

    # set the min and max numbers to 0 and 1, respectively
    numbers[greatest_number_index] = 1.0
    numbers[smallest_number_index] = 0.0

    # for all other numbers, their new values will be the distance between their current
    # value and the smallest number, divided by the distance between the smallest and
    # greatest numbers
    for number in numbers[1:-1]:
        numbers[numbers.index(number)] = (number - numbers[smallest_number_index]) / (
            numbers[greatest_number_index] - numbers[smallest_number_index]
        )

    return numbers

