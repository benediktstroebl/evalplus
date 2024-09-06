from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """

    # @TODO: Write a solution here
    # a = []
    # for n in numbers:
    #     if n not in a:
    #         a.append(n)
    # return a
    numbers_sorted = sorted(numbers)
    numbers_filtered = list(dict.fromkeys(numbers_sorted))
    numbers_filtered_sorted = sorted(numbers_filtered)
    return numbers_filtered_sorted

