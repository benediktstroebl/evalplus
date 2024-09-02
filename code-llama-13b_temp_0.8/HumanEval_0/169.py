from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """

    # The code below is just an example of what could go here.
    # This code doesn't work, but it is provided to help you write your own code.
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if abs(numbers[i] - numbers[j]) <= threshold:
                return True

    return False

    # HINT: You should use "for" loop to iterate over the list of numbers
    # and the nested "for" loop to check if any two numbers are close to each other.
    # Remember to return True if any pair of numbers are close to each other
    # and False if no pairs of numbers are close to each other.

