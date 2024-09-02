from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # TODO: implement me
    # You can start by trying an approach using O(n^2) time
    # Complexity: O(n^2)
    # Then try to improve it to linear time
    # Complexity: O(n)
    return list(set(numbers))

