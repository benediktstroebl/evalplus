from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # Check the length of the numbers list is at least two
    if len(numbers) < 2:
        return (0.0, 0.0)
    
    # Get the sorted list of numbers
    numbers = sorted(numbers)
    
    # Find the two numbers that are closest to each other
    smaller, larger = numbers[0], numbers[-1]
    for i in range(1, len(numbers) - 1):
        if numbers[i] > larger:
            larger = numbers[i]
        if numbers[i] < smaller:
            smaller = numbers[i]
    return smaller, larger