from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    # This has a complexity of O(n)
    # How many elements are in the list?
    # How many items are in the list?
    length = len(numbers)
    min_diff = 0.0
    min_diff_num1 = 0
    min_diff_num2 = 0

    # This will have a complexity of O(n)
    # The worst case is if the list is sorted and the items are equally spaced
    for x in range(length):
        for y in range(x + 1, length):
            diff = abs(numbers[x] - numbers[y])

            # This has a complexity of O(n)
            if diff < min_diff:
                min_diff = diff
                min_diff_num1 = numbers[x]
                min_diff_num2 = numbers[y]

    return (min_diff_num1, min_diff_num2)

