from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # init set with set O(1)
    duplicates = set()

    # iterate the list to check for duplicates O(n)
    for number in numbers:
        # if the number exists in the set it is a duplicate O(1)
        if number in duplicates:
            # skip the number O(1)
            continue
        # else add the number to the set O(1)
        duplicates.add(number)

    # return the list of all elements in the set in order O(n)
    return list(duplicates)

