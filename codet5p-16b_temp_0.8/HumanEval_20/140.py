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
        raise IndexError("There must be at least two numbers in the supplied list to find the closest pair.")
    numbers.sort()
    smallest = numbers[0]
    largest = numbers[-1]
    closest = [smallest, largest]
    for index in range(1, len(numbers) - 1):
        small = numbers[index]
        large = numbers[index + 1]
        if small < closest[0] and large > closest[1]:
            closest = [small, large]
        elif small < closest[0] and small == numbers[index - 1]:
            continue
        elif large > closest[1] and large == numbers[index + 2]:
            continue
        elif small > closest[0] and large < closest[1]:
            closest = [small, large]
    return tuple(closest)
