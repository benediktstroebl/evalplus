from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # To compare two numbers, use the absolute value of the difference as the key for a sored dictionary.
    # Find the nth smallest value in the list (the smallest means smallest difference, the second smallest means
    # second smallest difference, etc).
    smallest = min(numbers)
    # We are only interested in finding the closest elements, not their difference.
    # To find the difference between two elements, subtract the first element's value from the second element's value.
    # The resulting number is the difference. To find the absolute value of that number, use the builtin abs function.
    nearest = abs(numbers[0] - smallest)
    slowest = abs(numbers[0] - smallest)
    i = 1
    # Starting at the second element, compare its value to the value of the current smallest element.
    # Set the slowest element to the current element's value if it is less.
    while i < len(numbers):
        difference = abs(numbers[i] - smallest)
        if difference < nearest:
            nearest = difference
            slowest = numbers[i]
        i += 1
    return (smallest, slowest)

