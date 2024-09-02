from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    counter = {}
    for n in numbers:
        counter[n] = counter.get(n, 0) + 1
    result = []
    for n in numbers:
        if counter[n] == 1:
            result.append(n)
    return result

