from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    # create a new list that holds the differences between the elements
    # of the supplied list
    differences = []
    for index, number in enumerate(numbers):
        if index == 0:
            differences.append(number)
        else:
            differences.append(abs(number - numbers[index - 1]))

    # find the minimum difference
    minimum_difference = min(differences)

    # create a new list that holds the locations of the smallest differences
    # (the index of the minimum difference)
    minimum_difference_locations = []
    for index, number in enumerate(differences):
        if number == minimum_difference:
            minimum_difference_locations.append(index)

    # if the minimum difference is zero, all numbers are equal, so return
    # the first two numbers
    if minimum_difference == 0:
        return numbers[0], numbers[1]

    # if the number of locations is one, the minimum difference is between the
    # first and the last elements, so return them
    if len(minimum_difference_locations) == 1:
        if minimum_difference_locations[0] == 0:
            return numbers[0], numbers[1]
        elif minimum_difference_locations[0] == (len(numbers) - 1):
            return numbers[-1], numbers[-2]

    # if the number of locations is two, return the corresponding elements
    if len(minimum_difference_locations) == 2:
        return numbers[minimum_difference_locations[0]], numbers[minimum_difference_locations[1]]

