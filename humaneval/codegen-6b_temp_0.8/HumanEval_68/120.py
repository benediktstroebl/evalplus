
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
    arr = [x for x in arr if x != 0]
    if len(arr) == 0:
        return []
    elif len(arr) == 1:
        return [0, 1]
    else:
        arr.sort()
        smallest_even, smallest_index = 0, 0
        for i in range(len(arr)):
            if arr[i] % 2 == 0:
                if smallest_index == 0:
                    smallest_index, smallest_even = i, arr[i]
                else:
                    if arr[i] < smallest_even:
                        smallest_index, smallest_even = i, arr[i]
        return [smallest_even, smallest_index]

assert pluck([4,2,3,1]) == [2, 1]
assert pluck([1,2,3,4]) == [2, 1]
assert pluck([5, 0, 3, 0, 4, 2]) == [0, 1]
assert pluck([]) == []
assert pluck([1,2,3,4,5]) == [2, 3]
assert pluck([0, 42, 18, 120, 433, 682]) == [0, 4]
assert pluck([1, 2, 3, 0, 4, 2]) == [0, 1]
assert pluck([1, 1, 3, 4, 0, 0]) == [0, 2]
