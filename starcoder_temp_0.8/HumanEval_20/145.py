from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    # NOTE: Even though we are taking the absolute value, the floats will still be in the wrong order.

    # sort the array
    numbers.sort()

    # if all of the numbers in the array are the same, then all of the numbers will be returned as the smallest and
    # largest numbers
    if numbers[0] == numbers[-1]:
        return numbers[0], numbers[-1]

    # loop through the array and find the two numbers that are closest to each other
    closest_numbers = (numbers[0], numbers[0])
    for i in range(1, len(numbers) - 1):
        if abs(numbers[i] - numbers[i - 1]) < abs(numbers[i] - closest_numbers[0]):
            closest_numbers = (numbers[i - 1], numbers[i])
        elif abs(numbers[i] - numbers[i - 1]) > abs(numbers[i] - closest_numbers[1]):
            closest_numbers = (numbers[i], numbers[i - 1])

    return closest_numbers

