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
        raise ValueError("length of array must be greater than or equal to 2")

    smallest = numbers[0]
    biggest = numbers[0]
    closest_pair = (biggest, smallest)

    for n in numbers:
        if n < smallest:
            smallest = n
            closest_pair = (smallest, smallest)
        elif n > biggest:
            biggest = n
            closest_pair = (biggest, biggest)

    return closest_pair

