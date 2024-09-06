from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # We'll use a set to make sure each element in the output is unique
    # and we'll use an index to keep track of where we're inserting into
    # the output list
    output = []
    i = 0
    for num in numbers:
        if num not in output:
            output.append(num)
        else:
            i += 1

    return output

