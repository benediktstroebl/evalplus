from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    # Ensure the input is a list
    numbers = list(numbers)

    # Create a set of potentially close numbers
    close_numbers = set()
    for number in numbers:
        for current_number in numbers:
            if abs(current_number - number) <= threshold:
                close_numbers.add(number)
                close_numbers.add(current_number)

    # Return whether close numbers were found
    return bool(close_numbers)

