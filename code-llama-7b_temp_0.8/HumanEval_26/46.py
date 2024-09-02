from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    seen = set()

    def not_seen(number):
        return number not in seen

    for number in filter(not_seen, numbers):
        seen.add(number)

    return list(seen)

