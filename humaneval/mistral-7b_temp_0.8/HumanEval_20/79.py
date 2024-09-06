from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # Sort the numbers
    sorted_numbers = sorted(numbers)
    # Get the first and last element
    first_num, last_num = sorted_numbers[0], sorted_numbers[-1]
    # Get the absolute difference between the first and last element
    abs_diff = abs(first_num - last_num)
    # Iterate through the sorted numbers to find the two closest numbers
    for i in range(1, len(sorted_numbers) - 1):
        # Get the absolute difference between the i-th and the i+1-th element
        abs_diff_i = abs(sorted_numbers[i] - sorted_numbers[i + 1])
        # If the difference is smaller than the absolute difference between the first and last element, update the
        # absolute difference and the first and last number
        if abs_diff_i < abs_diff:
            abs_diff = abs_diff_i
            first_num, last_num = sorted_numbers[i], sorted_numbers[i + 1]
    return (first_num, last
