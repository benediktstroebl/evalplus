from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """

    # Main idea is to compare each number with each other number with bigger index,
    # if distance between them is smaller than given threshold, return True

    # O(n**2) time complexity, as it uses two nested loops

    if len(numbers) < 2:
        return False

    # Store lowest and highest indexes with numbers (starting from 1)
    min_index, max_index = 1, len(numbers) - 1

    for i in range(1, len(numbers)):
        if numbers[i] == numbers[min_index]:
            min_index += 1
        if numbers[i] == numbers[max_index]:
            max_index -= 1

    # Check if closest two numbers are closer than threshold
    return numbers[max_index] - numbers[min_index] < threshold

