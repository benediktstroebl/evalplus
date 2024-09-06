from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    numbers_size = len(numbers)
    if numbers_size < 2:
        raise ValueError("The length of the list must be at least two")
    elif numbers_size == 2:
        return numbers[0], numbers[1]
    else:
        current_smallest = float(numbers[0])
        current_largest = float(numbers[0])
        for number in numbers:
            if current_smallest > number:
                current_smallest = number
            elif current_largest < number:
                current_largest = number
        return current_smallest, current_largest

