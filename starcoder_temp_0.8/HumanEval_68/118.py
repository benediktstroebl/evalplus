
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
    from collections import deque
    queue = deque()

    for i in range(len(arr)):
        queue.append((arr[i], i))

    # odd - odd
    # even - even
    # odd - even
    # even - odd
    res = []
    while queue:
        node, i = queue.popleft()
        if not res and node % 2 == 0:
            res.append(node)
            res.append(i)
        elif node % 2 == 0 and node < res[0]:
            res.clear()
            res.append(node)
            res.append(i)
        elif node % 2 == 0 and node == res[0] and res[1] > i:
            res.clear()
            res.append(node)
            res.append(i)
        elif node % 2 == 1 and res:
            res.append(i)
            break

    return res

