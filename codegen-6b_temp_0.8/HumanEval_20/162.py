from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    if len(numbers) == 0:
        raise ValueError('List must have at least 2 elements')

    if len(numbers) < 2:
        raise ValueError('List must have at least 2 elements')

    if len(numbers) == 2:
        return numbers[0], numbers[1]

    # Find the distance to every number, and keep track of the closest two
    distances_to_the_current = [abs(number - numbers[0]) for number in numbers]
    closest_pair = (numbers[0], numbers[1])

    for i in range(1, len(numbers)):
        # Get the distance to the current number
        current_distance = abs(numbers[i] - numbers[0])

        # Check if we need to replace the smallest distance pair
        if current_distance < distances_to_the_current[0]:
            closest_pair = (numbers[i], numbers[0])
            distances_to_the_current[0] = current_distance

        # Check if we need to replace the second smallest distance pair
        elif current_distance < distances_to_the_current[1]:
            distances_to_the_current[1] = current_distance
            closest_pair = (numbers[i], numbers[1])

    return closest_pair[0], closest_pair[1]

