from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # Raise an AssertionError when the number of elements is less than 2
    assert len(numbers) >= 2, "The list of numbers must have at least 2 elements"
    # Sort the numbers in increasing order
    sorted_numbers = sorted(numbers)
    # Find the index of the smallest and the second smallest element
    index_of_smallest = sorted_numbers.index(sorted_numbers[0])
    index_of_second_smallest = sorted_numbers.index(sorted_numbers[1])
    # Return the smallest and the second smallest elements
    return sorted_numbers[index_of_smallest], sorted_numbers[index_of_second_smallest]
