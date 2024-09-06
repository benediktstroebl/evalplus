from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    # Make sure we have at least two numbers to work with
    if len(numbers) < 2:
        raise ValueError("list must contain at least two numbers")

    # Sort the numbers into ascending order
    numbers.sort()

    # Use index to identify the smallest and largest number
    smallest_index = 0
    largest_index = len(numbers) - 1

    # If the largest number is very close to the smallest,
    # return the smallest number and the next largest number
    if abs(numbers[largest_index] - numbers[smallest_index]) < 1e-10:
        return numbers[smallest_index], numbers[smallest_index + 1]

    # Otherwise, return the two numbers that are the closest
    # to each other
    for i in range(1, len(numbers) - 1):
        diff = abs(numbers[largest_index] - numbers[smallest_index])
        temp_diff = abs(numbers[largest_index] - numbers[i]) + abs(numbers[smallest
