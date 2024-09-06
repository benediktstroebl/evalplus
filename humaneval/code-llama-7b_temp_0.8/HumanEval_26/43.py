from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # Base case: Empty list, nothing to remove.
    if len(numbers) == 0:
        return numbers
    # Keep track of what we're adding to the output.
    output = [numbers[0]]
    # Loop over every element.
    for i in range(1, len(numbers)):
        # Check if the current element is the same as the last one.
        if numbers[i] != output[-1]:
            # If not, add it.
            output.append(numbers[i])
    return output

