from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # Initialize an empty list.
    result = []

    for number in numbers:
        # Check if the number is not in the list already.
        if number not in result:
            # If not, append it to the list.
            result.append(number)

    return result
