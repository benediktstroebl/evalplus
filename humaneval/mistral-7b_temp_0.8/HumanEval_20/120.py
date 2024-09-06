from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    # Use these lines to help with the first few lines of your solution:
    assert len(numbers) >= 2, "There must be at least two elements in the list of numbers to find the closest!"
    numbers.sort()
    second_closest_number = numbers[1]

    # Your code goes here
    # (1) Find the smallest two numbers that are as close to each other as possible
    # (2) Return the smaller and larger numbers
    if len(numbers) == 2:
        return numbers[0], numbers[1]
    else:
        if second_closest_number - numbers[0] < numbers[1] - second_closest_number:
            return numbers[0], second_closest_number
        else:
            return second_closest_number, numbers[1]
