from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    # 1. Sort the list in ascending order
    numbers.sort()

    # 2. Calculate the distance between the first two elements
    delta = numbers[1] - numbers[0]

    # 3. If the distance is zero, we are dealing with duplicates and will return the first two numbers
    if delta == 0:
        return numbers[0], numbers[1]

    # 4. If the distance is not zero, we will now check if we can improve on our first guess
    # by looking at the second and third elements
    new_delta = numbers[2] - numbers[1]
    if new_delta < delta:
        return numbers[1], numbers[2]
    else:
        return numbers[0], numbers[1]

