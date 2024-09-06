from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    length = len(numbers)
    if length == 0:
        raise ValueError("List must contain at least two elements")

    if length == 1:
        raise ValueError("List must contain at least two elements")

    if length == 2:
        return numbers[0], numbers[1]

    # We cannot use the iter() builtin since it is not supported, e.g. by the command line.
    list_copy = list(numbers)  # It is important to copy the list to avoid changing the list in the function.
    list_copy.sort()
    smallest = list_copy[0]
    second_smallest = list_copy[1]
    for i in range(2, length):
        if list_copy[i] - smallest <= second_smallest - smallest:
            second_smallest = smallest
            smallest = list_copy[i]
        elif list_copy[i] - smallest > second_smallest - smallest:
            second_smallest = list_copy[i]

    return smallest, second_smallest

