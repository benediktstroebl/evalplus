from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # Set to keep track of duplicates
    seen_numbers = set()
    # Output list to be filled
    output = []
    # Iterate through the input list
    for num in numbers:
        # If we have not seen this element before
        if num not in seen_numbers:
            # Add it to seen numbers and to the output
            seen_numbers.add(num)
            output.append(num)
    return output

