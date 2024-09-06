from typing import List
from itertools import accumulate
from collections import Counter
def pluck(arr: List[int]) -> List[int]:
    """
    Given an array representing a branch of a tree that has non-negative integer nodes,
    your task is to pluck one of the nodes and return it.

    The plucked node should be the node with the smallest even value.
    If multiple nodes with the smallest even value are found, return the node that has the smallest index.

    The plucked node should be returned in a list [smallest even value, its index].
    If there are no even values or the given array is empty, return [].

    Example:
    Input: [4,2,3]
    Output: [2, 1]

    Example:
    Input: [1,2,3]
    Output: [2, 1]

    Example:
    Input: []
    Output: []

    Example:
    Input: [5, 0, 3, 0, 4, 2]
    Output: [0, 1]
    """
    evens = [i for i, num in enumerate(arr) if num % 2 == 0]
    if not evens:
        return []
    _, indexes = Counter(evens).most_common(1)
    return [indexes[0], indexes[0]]