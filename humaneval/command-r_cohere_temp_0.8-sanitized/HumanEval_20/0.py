from typing import List, Tuple
def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return the two closest numbers 
    in the list and return them in order (smaller number first, larger number second).

    Parameters:
        numbers (List[float]): A list of at least two float numbers.

    Returns:
        Tuple[float, float]: Two closest numbers in the list in order.
    """
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two numbers")

    min_dist = numbers[1] - numbers[0]  # Initialize min distance between first two elements
    closest_elements = (numbers[0], numbers[1])  # Initialize closest elements

    for i in range(1, len(numbers) - 1):  # Iterate through the list, skipping first and last elements
        left_dist = numbers[i] - numbers[i - 1]
        right_dist = numbers[i + 1] - numbers[i]

        if left_dist < min_dist:
            min_dist = left_dist
            closest_elements = (numbers[i - 1], numbers[i])

        if right_dist < min_dist:
            min_dist = right_dist
            closest_elements = (numbers[i], numbers[i + 1])

    return closest_elements