from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # An example:
    # [1.0, 2.0, 3.0, 4.0, 5.0, 2.2]
    # 1.0 - 2.0 = 1
    # 1.0 - 3.0 = 2
    # 1.0 - 4.0 = 3
    # 1.0 - 5.0 = 4
    # 2.0 - 3.0 = 1
    # 2.0 - 4.0 = 2
    # 2.0 - 5.0 = 3
    # 3.0 - 4.0 = 1
    # 3.0 - 5.0 = 2
    # 4.0 - 5.0 = 1
    # 2.2 - 5.0 = 2.8

    # Step 1: sort the numbers in ascending order.
    # nums_sorted = [1.0, 2.0, 3.0, 4.0, 5.0, 
