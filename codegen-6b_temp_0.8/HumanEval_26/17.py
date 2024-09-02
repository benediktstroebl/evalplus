from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # Set with duplicates removed (elements in output will be unique)
    no_dups = set(numbers)
    # Output
    output = []
    # Iterate over elements in given list
    for num in numbers:
        # If element is not in set, add
        if num not in no_dups:
            output.append(num)
    # return list
    return output

