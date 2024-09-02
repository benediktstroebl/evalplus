from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # sort the input list
    numbers.sort()
    # initialize a counter for each element
    counter = {num: 0 for num in numbers}
    # loop through the list
    for num in numbers:
        # increment the counter if this is the first time this element has been seen
        if num not in counter:
            counter[num] = 1
        else:
            # if the counter is greater than 1, the element has been seen more than once, so remove it
            counter[num] -= 1
            if counter[num] == 0:
                del counter[num]
    return counter.keys()
