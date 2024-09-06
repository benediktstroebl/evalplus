from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    # find the smallest and largest numbers in the list
    smallest = numbers[0]
    largest = numbers[0]

    for i in numbers:
        if i < smallest:
            smallest = i
        elif i > largest:
            largest = i

    # find the two numbers that are closest to each other
    closests = []

    for i in numbers:
        closests.append((i - smallest, i - largest))

    minimum = min(closests, key=lambda x: x[0] + x[1])

    return (minimum[0], minimum[1])

