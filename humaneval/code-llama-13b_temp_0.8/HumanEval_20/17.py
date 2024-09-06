from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    numbers_list = sorted(numbers)
    index1 = 0
    index2 = 1
    while index2 < len(numbers_list):
        num1 = numbers_list[index1]
        num2 = numbers_list[index2]
        if num2 - num1 < numbers_list[index2 + 1] - num1:
            index2 += 1
        else:
            break
    return numbers_list[index1], numbers_list[index2]

