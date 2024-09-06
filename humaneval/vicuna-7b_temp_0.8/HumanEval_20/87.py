from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    first_closest = float('inf')
    second_closest = float('-inf')
    first_closest_index = 0
    second_closest_index = 0
    for i in range(1, len(numbers)):
        if numbers[i] < numbers[first_closest_index]:
            first_closest = numbers[i]
        elif numbers[i] == numbers[first_closest_index]:
            first_closest_index += 1
        else:
            second_closest = numbers[i]
            second_closest_index = i
            break
    return first_closest, second_closest