from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # loc = []
    # for i in range(len(numbers)):
    #     if i > 0 and numbers[i] == numbers[i - 1]:
    #         continue
    #     loc.append(i)

    # return [numbers[i] for i in loc]
    return sorted(set(numbers), key=numbers.index)

