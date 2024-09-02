from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    ret_val: Tuple[float, float] = (numbers[0], numbers[0])
    for index in range(1, len(numbers)):
        if abs(numbers[index] - numbers[index - 1]) < abs(ret_val[0] - ret_val[1]):
            ret_val = (numbers[index], ret_val[1])
        elif abs(numbers[index] - numbers[index - 1]) == abs(ret_val[0] - ret_val[1]):
            if numbers[index] < ret_val[1]:
                ret_val = (numbers[index], ret_val[1])
            else:
                ret_val = (ret_val[0], numbers[index])
    return tuple(sorted(ret_val))

