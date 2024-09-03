from typing import List, Tuple
def find_closest_elements(numbers: List[float]):
    """ Selects two elements from the list that are the closest to each other and returns them in order (smaller number, larger number).
    Args:
        - numbers: List of float, length at least two
    Returns:
        - Tuple of two float numbers, the two closest elements
    """
    if len(numbers) < 2:
        return ()
    else:
        # Sort the list of numbers in ascending order
        numbers.sort()
        # are closest first and second elements
        return numbers[0:1]
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 8.0]