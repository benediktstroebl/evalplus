from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    # check if there are any duplicates within the list
    numbers_set = set(numbers)

    for number in numbers_set:
        # check if there is any other number in the list that is close to the current number
        for other_number in numbers_set:
            if abs(number - other_number) < threshold:
                return True

    return False

