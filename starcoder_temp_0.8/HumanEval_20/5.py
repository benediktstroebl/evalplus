from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # Sort the list
    sorted_numbers = sorted(numbers)

    # Get the min distance of the two numbers
    min_distance = abs(sorted_numbers[0] - sorted_numbers[1])

    # Get the first two numbers of the sorted list
    first_number, second_number = sorted_numbers[0], sorted_numbers[1]

    # For each number in the sorted list
    for number in sorted_numbers[2:]:
        # Check for the minimum distance
        if abs(number - first_number) < min_distance:
            # If the current distance is less than the minimum distance
            # replace the first number and second number
            min_distance = abs(number - first_number)
            second_number = number

    # Return the smallest and the largest number
    return first_number, second_number

