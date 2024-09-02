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
        raise ValueError("List of numbers must be at least 2 elements long.")

    sorted_numbers = sorted(numbers)

    if abs(sorted_numbers[-1] - sorted_numbers[0]) <= 1e-6:
        return sorted_numbers[0], sorted_numbers[-1]

    low_index, high_index = 0, len(numbers) - 1

    while low_index < high_index:
        mid_index = (low_index + high_index) // 2

        mid_number = sorted_numbers[mid_index]
        mid_distance = get_distance_between(mid_number, sorted_numbers[0])
        mid_distance_big = get_distance_between(mid_number, sorted_numbers[-1])

        if mid_distance_big < mid_distance:
            high_index = mid_index
        elif mid_distance_big > mid_distance:
            low_index = mid_index + 1
        elif abs(mid_distance) - 0.5 < 1e-6:
            return get_closest_element(sorted_numbers[mid_index], sorted_numbers[low_index]), \
                   get_closest_element(sorted_numbers[high_index], sorted_numbers[low_index])
        else:
            return get_closest_element(sorted_numbers[mid_index], sorted_numbers[low_index]), \
                   get_closest_element(sorted_numbers[high_index], sorted_numbers[low_index])

    if abs(sorted_numbers[low_index] - sorted_numbers[high_index]) <= 1e-6:
        return sorted_numbers[low_index], sorted_numbers[high_index]

    return get_closest_element(sorted_numbers[low_index], sorted_numbers[high_index]), \
           get_closest_element(sorted_numbers[high_index], sorted_numbers[low_index])

