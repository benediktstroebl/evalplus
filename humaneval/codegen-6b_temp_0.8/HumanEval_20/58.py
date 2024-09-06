from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    if len(numbers) >= 2:
        numbers = sorted(numbers)
        smallest = numbers[0]
        largest = numbers[-1]
        second_smallest = numbers[1]
        for x in numbers:
            if abs(x - smallest) > abs(x - second_smallest):
                second_smallest = smallest
                smallest = x
            if abs(x - largest) > abs(x - second_smallest):
                second_smallest = largest
                largest = x
        return smallest, second_smallest
    else:
        raise ValueError("More than one number needed in function")

