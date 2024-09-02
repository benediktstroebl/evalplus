from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    # 1. Brute force approach:
    # for i in range(len(numbers) - 1):
    #     current_closest = min(numbers[i], numbers[i + 1])
    #     if abs(numbers[i] - numbers[i + 1]) < current_closest:
    #         current_closest = abs(numbers[i] - numbers[i + 1])
    #         current_numbers = (numbers[i], numbers[i + 1])
    # return current_numbers

    # 2. Optimized approach - using list comprehension:
    # a_list = list(enumerate(numbers))
    # sorted_by_second = sorted(a_list, key=lambda x: x[1])
    # ordered = [x[1] for x in sorted_by_second]
    # first = ordered[0]
    # second = ordered[1]
    # smallest_distance = abs(first - second)
    # for i in range(len(ordered) - 1):
    #     first = ordered[i]
    #     second = ordered[i + 1]
    #     if abs(first - second) < smallest_distance:
    #         smallest_distance = abs(first - second)
    #         current_numbers = (first, second)
    # return current_numbers

    # 3. Optimized approach - using list comprehension and using an intermediate list (not very efficient but I
    #  decided to write it for practice):
    a_list = list(enumerate(numbers))
    sorted_by_second = sorted(a_list, key=lambda x: x[1])
    ordered = [x[1] for x in sorted_by_second]
    first = ordered[0]
    smallest_distance = abs(first - ordered[1])
    current_numbers = (first, ordered[1])
    for i in range(len(ordered) - 1):
        first = ordered[i]
        second = ordered[i + 1]
        if abs(first - second) < smallest_distance:
            smallest_distance = abs(first - second)
            current_numbers = (first,
