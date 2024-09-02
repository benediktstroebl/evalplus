from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    # Raise an error if numbers is not a list
    if type(numbers)!= list:
        raise TypeError("numbers must be of type list.")

    # Raise an error if numbers is empty
    if len(numbers) < 2:
        raise TypeError("numbers must contain at least two elements.")

    # Raise an error if any number in numbers is not a float
    for number in numbers:
        if type(number)!= float:
            raise TypeError("numbers must be a list containing only float values.")

    # Sort the list in ascending order
    numbers.sort()

    # Return the first and last number in the sorted list
    return numbers[0], numbers[-1]

