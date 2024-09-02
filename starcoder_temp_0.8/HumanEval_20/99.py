from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    diff_list = [abs(x - numbers[i]) for i, x in enumerate(numbers)]
    index_of_smallest = diff_list.index(min(diff_list))
    index_of_largest = diff_list.index(max(diff_list))
    smallest = numbers[index_of_smallest]
    largest = numbers[index_of_largest]
    if smallest > largest:
        return largest, smallest
    else:
        return smallest, largest
