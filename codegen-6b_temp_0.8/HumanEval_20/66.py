from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # Sort the given numbers
    numbers = sorted(numbers)

    # Do some statistics (your code here)
    if len(numbers) < 2:
        raise Exception("Too few values to sort")

    # (your code here)
    if numbers[0] == numbers[1]:
        return numbers[0], numbers[0]
    result = (numbers[0], numbers[1])
    for index in range(2, len(numbers)):
        current = numbers[index]
        prev = numbers[index - 1]
        prevprev = numbers[index - 2]
        if current - prev > result[1] - result[0]:
            if current - prevprev > result[1] - result[0]:
                result = (current, prevprev)
            else:
                result = (prevprev, current)
        elif current - prev < result[1] - result[0]:
            if current - prevprev < result[1] - result[0]:
                result = (prev, current)
            else:
                result = (prevprev, current)
    return result

