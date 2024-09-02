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
        raise ValueError("list must have at least two numbers")
    min_difference = float("inf")
    selected_numbers = []
    smaller_num = None
    larger_num = None
    for i in range(len(numbers) - 1):
        first_num = numbers[i]
        second_num = numbers[i + 1]
        abs_first_num = abs(first_num)
        abs_second_num = abs(second_num)
        if abs_first_num < abs_second_num:
            smaller_num = first_num
            larger_num = second_num
        else:
            smaller_num = second_num
            larger_num = first_num
        current_difference = abs(smaller_num - larger_num)
        if current_difference < min_difference:
            min_difference = current_difference
            selected_numbers = [smaller_num, larger_num]
    return selected_numbers[0], selected_numbers[1]

