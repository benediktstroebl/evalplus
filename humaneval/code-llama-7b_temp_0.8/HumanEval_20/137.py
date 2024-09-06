from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    # select first number
    current_number = numbers[0]
    current_closest_distance = None

    # loop through numbers
    for number in numbers:
        if current_closest_distance is None:
            current_closest_distance = number - current_number
        else:
            current_closest_distance = min(
                current_closest_distance, number - current_number
            )

    # store closest numbers
    first_closest_number = None
    second_closest_number = None

    # loop through numbers
    for number in numbers:
        difference_to_first_closest = abs(number - first_closest_number)
        difference_to_second_closest = abs(number - second_closest_number)
        difference_to_number = number - current_number

        if (
            difference_to_first_closest > difference_to_number
            or difference_to_second_closest > difference_to_number
        ):
            if first_closest_number is None:
                first_closest_number = number
            elif second_closest_number is None:
                second_closest_number = number

    return first_closest_number, second_closest_number

