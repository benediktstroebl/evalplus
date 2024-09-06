from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # Find the maximum and minimum numbers in the list
    max_num = max(numbers)
    min_num = min(numbers)

    # Find the average of the two numbers
    avg_num = (max_num + min_num) / 2

    # Find the closest numbers to the maximum and minimum numbers
    closest_max = numbers[0] if numbers[0] <= max_num else max_num
    closest_min = numbers[-1] if numbers[-1] >= min_num else min_num

    # If the closest_max is less than the maximum number, adjust it
    if closest_max < max_num:
        closest_max = max_num
    # If the closest_min is greater than the minimum number, adjust it
    if closest_min > min_num:
        closest_min = min_num

    return avg_num, closest_min

