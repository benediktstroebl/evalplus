from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # first, sort list in ascending order
    numbers.sort()

    # next, find index of min and max values
    min_index = numbers.index(min(numbers))
    max_index = numbers.index(max(numbers))

    # if min and max are at the same index, the min value is also the max value
    if min_index == max_index:
        return (numbers[min_index], numbers[max_index])

    # find the absolute difference between min and max
    difference = abs(max_index - min_index)

    # if the absolute difference is greater than 1 (1 index away), the min value is the larger of the two
    if difference > 1:
        return (numbers[min_index], numbers[min(max_index, min_index + 1)])

    # else, min value is the min value and max value is the larger of the two
    return (numbers[min_index], numbers[max(max_index, min_index + 1)])

