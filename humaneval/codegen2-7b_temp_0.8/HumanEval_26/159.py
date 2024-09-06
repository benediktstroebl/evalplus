from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    seen: List[int] = []
    seen_add: Callable[[int], None] = seen.add
    return [x for x in numbers if not (x in seen or seen_add(x))
