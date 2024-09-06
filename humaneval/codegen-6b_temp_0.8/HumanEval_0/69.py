from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    dict_numbers = {}
    for num in numbers:
        dict_numbers[num] = 1

    for num in dict_numbers:
        if dict_numbers[num] > 1:
            for i in range(dict_numbers[num]):
                if (num - threshold) in dict_numbers and (num + threshold) in dict_numbers:
                    return True
    return False

