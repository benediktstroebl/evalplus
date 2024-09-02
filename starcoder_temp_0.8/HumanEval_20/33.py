from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    # we can just take advantage of built in list functions
    smallest, largest = min(numbers), max(numbers)
    # we know the answer is going to be in between these two numbers so we can make a guess that it will be
    # the smallest number in between the two
    guess = smallest + (largest - smallest) / 2

    # we can check this guess by iterating through the list and seeing if we can narrow it down to two items
    for number in numbers:
        # if our guess is closer to the number than the current smallest number we found so far, then we update
        # the smallest number to be our guess
        if abs(number - guess) < abs(smallest - guess):
            smallest = number
        # if our guess is closer to the number than the current largest number we found so far, then we update
        # the largest number to be our guess
        if abs(number - guess) > abs(largest - guess):
            largest = number

    return smallest, largest
