from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # set is a built-in datastructure which is an unordered collection of
    # elements. They're similar to lists and dicts except they contain
    # only unique elements, with no duplicate values.
    # set([1, 2, 2, 3, 3, 3, 4, 5, 6, 6])
    # {1, 2, 3, 4, 5, 6}
    # set({1, 2, 2, 3, 3, 3, 4, 5, 6, 6})
    # {1, 2, 3, 4, 5, 6}
    # set(frozenset([1, 2, 2, 3, 3, 3, 4, 5, 6, 6]))
    # {1, 2, 3, 4, 5, 6}
    seen = set()
    for number in numbers:
        if number not in seen:
            yield number
            seen.add(number)

