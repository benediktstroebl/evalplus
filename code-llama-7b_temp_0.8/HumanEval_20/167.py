from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # Check that numbers has length at least 2
    if len(numbers) < 2:
        raise ValueError('Numbers has length less than 2')

    # Create a copy of numbers so that we can sort it without changing the original list
    numbers_copy = numbers.copy()

    # Sort the list in ascending order
    numbers_copy.sort()

    # Pick out the two closest numbers
    smallest_diff = numbers_copy[1] - numbers_copy[0]
    closest_numbers = (numbers_copy[0], numbers_copy[1])

    # Loop over all the numbers in the list (skip the first two)
    for i in range(2, len(numbers_copy)):
        # Check if the current number is closer to the previous one than the last closest pair
        if numbers_copy[i] - numbers_copy[i - 1] < smallest_diff:
            # Store the difference and the pair of numbers
            smallest_diff = numbers_copy[i] - numbers_copy[i - 1]
            closest_numbers = (numbers_copy[i - 1], numbers_copy[i])

    return closest_numbers

