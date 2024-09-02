from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    len_numbers = len(numbers)
    if len_numbers < 2:
        raise ValueError("At least two numbers are needed.")
    min_distance_index = 0
    min_distance = float('inf')
    for index in range(len_numbers):
        distance = numbers[index] - numbers[index - 1]
        if distance < min_distance:
            min_distance = distance
            min_distance_index = index - 1
    first_num = numbers[min_distance_index]
    second_num = numbers[min_distance_index + 1]
    return (first_num, second_num)
    # return (2.0, 2.2)
    # return (2.0, 2.0)

