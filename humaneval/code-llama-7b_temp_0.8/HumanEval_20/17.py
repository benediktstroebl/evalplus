from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    # Min and max to store the minimum distance and pair
    min_dist = float("inf")
    min_pair = tuple()

    # Let's loop through the list
    for index, num in enumerate(numbers):

        # We calculate the distance of num to the first number in the list and add it to the min_dist if it is smaller
        # than it
        dist_to_first = abs(num - numbers[0])
        if dist_to_first < min_dist:
            min_dist = dist_to_first
            min_pair = (numbers[0], num)

        # We do the same for the last number
        dist_to_last = abs(num - numbers[-1])
        if dist_to_last < min_dist:
            min_dist = dist_to_last
            min_pair = (numbers[-1], num)

        # We find the closest pair for all the other numbers
        for num2 in numbers[index + 1:]:

            # If the absolute value between them is smaller than our current minimum we change it
            dist_to_pair = abs(num - num2)
            if dist_to_pair < min_dist:
                min_dist = dist_to_pair
                min_pair = (num, num2)

    return min_pair

