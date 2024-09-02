from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    # Make a list of tuples (i, j) where i is the index of the list of numbers and j is the value of the index
    index_value_list = [(i, v) for i, v in enumerate(numbers)]
    index_value_list = sorted(index_value_list, key=lambda x: x[1])
    i1, v1 = index_value_list[0]
    i2, v2 = index_value_list[1]
    v2_diff = v1 - v2
    return (numbers[i1], numbers[i2]) if v2_diff > 0 else (numbers[i2], numbers[i1])
