from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """

    # The smallest number in the list
    smallest = min(numbers)
    # The largest number in the list
    largest = max(numbers)
    # Calculate the size of our range
    range_size = largest - smallest
    # Create our new list of numbers
    new_list = []
    for number in numbers:
        # Calculate the difference between the number and the smallest
        diff = number - smallest
        # Scale our difference
        scaled_diff = diff / range_size
        # Append our scaled number to our new list
        new_list.append(scaled_diff)
    return new_list

