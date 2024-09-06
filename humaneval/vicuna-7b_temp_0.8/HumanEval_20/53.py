from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # Select the smallest and largest numbers from the list of numbers
    smallest = min(numbers)
    largest = max(numbers)

    # Define a variable to keep track of the closest pair of numbers
    closest_pair = (smallest, largest)

    # Iterate through the list of numbers and find the closest pair
    for i in range(1, len(numbers)):
        smaller_number, smaller_closest = find_closest_element(numbers[i:])
        larger_number, larger_closest = find_closest_element(numbers[i:])

        # If the closest pair of numbers has not been found yet, swap the closest pair with the smallest and largest numbers
        if smaller_closest is None:
            smallest, largest = largest, smallest

        # Compare the closest pair of numbers to the current smallest and largest numbers
        distance = abs(smallest - smaller_number) + abs(largest - larger_number)
        if distance < closest_pair[1] - smallest:
            smallest, largest, closest_pair = smallest, larger_number, largest, smallest

    return closest_pair
