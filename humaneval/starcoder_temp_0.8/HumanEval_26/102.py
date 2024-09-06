from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # for i in numbers:
    #     for j in numbers[numbers.index(i) + 1:]:
    #         if i == j:
    #             numbers.remove(j)
    # return numbers

    # Using set()
    return list(set(numbers))

