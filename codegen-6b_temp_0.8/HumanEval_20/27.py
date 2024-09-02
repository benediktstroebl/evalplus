from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    """Bubble Sort"""
    """It's the first algorithm to solve the sort problem.
    It's the simplest algorithm to follow in a way of thinking.
    It's the simplest algorithm to follow in a way of thinking backwards."""
    if len(numbers) < 2:
        raise ValueError('Must have at least two numbers in array')
    # We will store the length of the list to ensure the loop below runs.
    list_length = len(numbers)
    # Its a simple loop that iterates over the list and compares the values,
    # and pushes smallest values to the left.
    for i in range(list_length):
        # It will compare the first two elements, and move it out to the right.
        for j in range(i + 1, list_length):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    # We will return the two closest elements.
    return numbers[0], numbers[list_length - 1]

