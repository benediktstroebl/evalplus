from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    numbers_size = len(numbers)
    first_number_index = 0
    second_number_index = 1

    smallest_difference_between_two_numbers = abs(numbers[first_number_index] - numbers[second_number_index])

    for first_number_index in range(numbers_size - 1):
        for second_number_index in range(first_number_index + 1, numbers_size):
            current_difference_between_two_numbers = abs(numbers[first_number_index] - numbers[second_number_index])
            if current_difference_between_two_numbers < smallest_difference_between_two_numbers:
                smallest_difference_between_two_numbers = current_difference_between_two_numbers
                first_number_with_smallest_difference = numbers[first_number_index]
                second_number_with_smallest_difference = numbers[second_number_index]

    return first_number_with_smallest_difference, second_number_with_smallest_difference

