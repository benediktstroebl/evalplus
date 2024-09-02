from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    if len(numbers) < 2:
        raise ValueError("List must be of length at least two")

    # Set initial values
    first_number, second_number = numbers[0], numbers[1]
    first_index, second_index = 0, 1

    # Loop through each number, and if that number is closer to the first_number than the second number, it becomes
    # the second number. If it's the other way around, it becomes the first number.
    for index, number in enumerate(numbers):
        if abs(number - first_number) < abs(number - second_number):
            second_number = number
            second_index = index
        elif abs(number - first_number) > abs(number - second_number):
            first_number = number
            first_index = index

    return (
        numbers[first_index],
        numbers[second_index]
    )

