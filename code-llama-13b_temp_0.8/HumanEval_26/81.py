from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # time O(N) where N is length of numbers
    # space O(N) where N is length of numbers
    seen = set()
    result = []
    for number in numbers:
        if number not in seen:
            result.append(number)
            seen.add(number)
    return result

