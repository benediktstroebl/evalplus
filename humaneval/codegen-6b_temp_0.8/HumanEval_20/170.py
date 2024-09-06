from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # your code here

    # The function should return 2 closest elements in the list and the elements will be returned in ascending order.
    # For example, if the list is [1.0, 2.0, 3.0, 4.0, 5.0, 2.2] then the function should return (2.0, 2.2)
    # since 2.0 is the closest to 2.2.

    # Choosing the smallest abs(difference) element as the first element and the largest abs(difference) element as the
    # second element.
    # Searching for the smallest absolute value element between these two
    #  elements
    # Searching for the largest absolute value element between these two
    #  elements
    # Building a new sorted list of the two smallest absolute values elements.
    # Returning these elements in order.

    # In the case where the list has only one element, return the first element and its absolute value.

    if len(numbers) < 2:
        raise ValueError('Need a list of length at least two')

    if len(numbers) == 2:
        return numbers[0], numbers[1]

    if len(numbers) == 3:
        return numbers[0], numbers[2]

    # start the search for min or max value in the list
    smallest_abs_diff = max(abs(numbers[0] - numbers[1]), abs(numbers[0] - numbers[2]))
    largest_abs_diff = abs(numbers[1] - numbers[2])

    numbers.sort()

    # Take the first number from the list and the last number from the list
    smallest_abs_diff_element = numbers[0]
    largest_abs_diff_element = numbers[-1]

    if smallest_abs_diff == 0:
        return smallest_abs_diff_element, largest_abs_diff_element

    # Search for the smallest absolute value element between these two
    # elements in the list

    for i in range(len(numbers) - 1):
        if abs(numbers[i] - numbers[i + 1]) < smallest_abs_diff:
            smallest_abs_diff_element = numbers[i]
