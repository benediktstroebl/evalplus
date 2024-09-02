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
        return (float('inf'), float('inf'))

    smallest = numbers[0]
    largest = numbers[0]

    for number in numbers:
        smallest = min(smallest, number)
        largest = max(largest, number)

    closest_pair = (smallest, largest)

    for number in numbers:
        if number < smallest:
            smallest = number
        elif number > largest:
            largest = number

    return closest_pair

