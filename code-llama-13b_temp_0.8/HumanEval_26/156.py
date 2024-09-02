from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # Approach 1: sort the list and remove duplicates
    # numbers.sort()
    # last = None
    # for i in range(len(numbers)):
    #     if last == numbers[i]:
    #         numbers.pop(i)
    #     else:
    #         last = numbers[i]
    # return numbers

    # Approach 2: using a set
    return list(set(numbers))

