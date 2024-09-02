from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # Sort the numbers in ascending order
    sorted_numbers = sorted(numbers)

    # Initiate the closest numbers variable to a tuple of the two closest numbers to each other in the list of numbers
    closest_numbers = (sorted_numbers[0], sorted_numbers[1])
    # Initiate the first_closest_distance variable to the distance between the first two closest numbers in the list
    # of numbers
    first_closest_distance = closest_numbers[1] - closest_numbers[0]

    # For every number in the list of numbers
    for i in range(len(sorted_numbers)):
        # If the current number is not the first or last number
        if i != 0 and i != len(sorted_numbers) - 1:
            # Find the difference between the current number and the next number
            current_next_distance = sorted_numbers[i + 1] - sorted_numbers[i]
            # If the current next distance is smaller than the first closest distance
            if current_next_distance < first_closest_distance:
                # Set the first closest distance to the current next distance
                first_closest_distance = current_next_distance
                # Set the closest numbers to the current number and the next number
                closest_numbers = (sorted_numbers[i], sorted_numbers[i + 1])
        # Else if the current number is the last number
        elif i == len(sorted_numbers) - 1:
            # Find the difference between the current number and the previous number
            current_previous_distance = sorted_numbers[i - 1] - sorted_numbers[i]
            # If the current previous distance is smaller than the first closest distance
            if current_previous_distance < first_closest_distance:
                # Set the first closest distance to the current previous distance
                first_closest_distance = current_previous_distance
                # Set the closest numbers to the current number and the previous number
                closest_numbers = (sorted_numbers[i - 1], sorted_numbers[i])

    # Return the closest numbers
    return closest_numbers

