from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # create a list of the distances between each number and the previous number
    distances = [abs(numbers[i] - numbers[i - 1]) for i in range(1, len(numbers) + 1)]

    # calculate the average of the distances
    average_distance = sum(distances) / len(distances)

    # find the two numbers that are closest by taking the first and second closest numbers
    closest_numbers = sorted(numbers, key=lambda x: abs(x - average_distance), reverse=True)

    # return the two numbers
    return closest_numbers[0], closest_numbers[1]

