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
        raise ValueError("The input list must contain at least two numbers.")

    # Find the smallest and largest number in the list
    min_num, max_num = numbers[0], numbers[-1]
    for num in numbers[1:-1]:
        if num < min_num:
            min_num = num
        elif num > max_num:
            max_num = num

    # Find the two numbers closest to the middle of the range
    middle_num = (min_num + max_num) / 2
    closest_num_1 = find_closest_element(numbers, middle_num)
    closest_num_2 = find_closest_element(numbers, middle_num, 1)

    return closest_num_1, closest_num_2

