from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # initialize a dictionary to count the number of times each element appears
    count = {}
    for element in numbers:
        if element in count:
            count[element] += 1
        else:
            count[element] = 1

    # return the elements with a count of 1
    return [key for key in count if count[key] == 1]

