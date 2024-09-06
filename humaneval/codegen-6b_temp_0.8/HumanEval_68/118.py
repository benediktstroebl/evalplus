
def pluck(arr):
    """
    "Given an array representing a branch of a tree that has non-negative integer nodes
    your task is to pluck one of the nodes and return it.
    The plucked node should be the node with the smallest even value.
    If multiple nodes with the same smallest even value are found return the node that has smallest index.

    The plucked node should be returned in a list, [ smalest_value, its index ],
    If there are no even values or the given array is empty, return [].

    Example 1:
        Input: [4,2,3]
        Output: [2, 1]
        Explanation: 2 has the smallest even value, and 2 has the smallest index.

    Example 2:
        Input: [1,2,3]
        Output: [2, 1]
        Explanation: 2 has the smallest even value, and 2 has the smallest index. 

    Example 3:
        Input: []
        Output: []
    
    Example 4:
        Input: [5, 0, 3, 0, 4, 2]
        Output: [0, 1]
        Explanation: 0 is the smallest value, but  there are two zeros,
                     so we will choose the first zero, which has the smallest index.

    Constraints:
        * 1 <= nodes.length <= 10000
        * 0 <= node.value
    """
    return [sorted(arr, key=lambda x: (x%2, x))[0], arr.index(sorted(arr, key=lambda x: (x%2, x))[0])] if arr else []


"""
scatter and sort

Given a list of integers off a single branch of a tree, find the node on that branch
with the maximum integer value. Then, remove that value from the list.
Continue until the list is empty.

Example 1:
    Input: [1, 2, 3, 4, 5, 6]
    Output: 5
    Explanation:
    1 -> 5
    2 -> 4
    3 -> 6
    4 -> 3
    5 -> 1
    6 -> 2

Example 2:
    Input: [5, 6, 7, 8, 9]
    Output: 8
    Explanation:
    5 -> 8
    6 -> 9
    7 -> 8
    8 -> 6
    9 -> 5

Example 3:
    Input: [1, 2, 3, 4]
    Output: 4
    Explanation:
    1 -> 4
    2 -> 1
    3 -> 2
    4 -> 3

https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bst/description/
"""