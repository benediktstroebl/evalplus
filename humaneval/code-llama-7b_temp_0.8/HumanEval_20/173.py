from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # To solve this, we can do the following:
    # 1. Use a nested loop. Outer loop iterates from 0 to len(numbers)-1, inner loop from outer+1 to len(numbers)
    # 2. In each iteration, calculate the difference between the two numbers.
    # 3. If the difference is the smallest we've seen, save those two numbers

    min_diff = float("inf")
    min_pair = None

    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            diff = abs(numbers[i] - numbers[j])
            if diff < min_diff:
                min_diff = diff
                min_pair = (numbers[i], numbers[j])

    return min_pair

