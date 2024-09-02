from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # My first attempt at solving this problem:
    # seen = set()
    # seen_add = seen.add
    # unique = [x for x in numbers if not (x in seen or seen_add(x))]
    # return unique

    # My second attempt (see #397):
    seen = set()
    unique = [n for n in numbers if n not in seen]
    seen.update(unique)
    return unique
