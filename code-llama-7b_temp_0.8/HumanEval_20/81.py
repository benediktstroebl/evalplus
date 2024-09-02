from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # detect if there are less than two elements in the list
    if len(numbers) < 2:
        raise ValueError("list length must be at least two")

    # iterate through the list and find the two elements that are closest to each other
    closest_pair = (0, 1)
    smallest_distance = abs(numbers[0] - numbers[1])

    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if abs(numbers[i] - numbers[j]) < smallest_distance:
                smallest_distance = abs(numbers[i] - numbers[j])
                closest_pair = (i, j)

    return numbers[closest_pair[0]], numbers[closest_pair[1]]

