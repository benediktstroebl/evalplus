from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    if len(numbers) < 2:
        return False

    # Don't need to build list if it is already sorted.
    if min(numbers) == max(numbers):
        return False

    # Iterate through each number.
    # If the number is the same as the previous number, then skip by incrementing i
    # such that the next number can be found.
    # Then, loop through the number again and start from i and j.
    i = 0
    while i < len(numbers):
        j = i + 1
        while j < len(numbers):
            if abs(numbers[i] - numbers[j]) <= threshold:
                return True
            j += 1
        i += 1
    return False

