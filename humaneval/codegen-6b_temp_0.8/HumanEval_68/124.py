
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
    # brute force: try all possible combinations
    # find the largest even value, and return the node with smallest index
    # if even vals are not found, return empty list

    def isEven(n):
        return n % 2 == 0

    def minIndex(arr):
        if not arr:
            return []
        idx = 0
        minVal = arr[0]
        for i in range(len(arr)):
            if isEven(arr[i]) and arr[i] < minVal:
                idx = i
                minVal = arr[i]

        return [idx, minVal]

    def pluck(arr):
        if not arr:
            return []
        if isEven(arr[0]):
            return [arr[0], 0]
        # only need to search the even values
        # use minIndex to figure out which is the smallest
        # if found non-duplicate, return the index, which is the node with smallest index
        # if not, find the duplicated node, and return the index of the node
        firstOdd, otherOdd = [], []
        d = {}
        for i in range(len(arr)):
            if isEven(arr[i]):
                d[arr[i]] = i
            else:
                firstOdd.append(arr[i])
        n = minIndex(firstOdd)
        if n:
            return n
        return [minIndex(otherOdd)]

    return pluck(arr)
