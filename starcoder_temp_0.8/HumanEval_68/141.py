
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
    # def find_smallest(self, node):
    #     if node is None:
    #         return None

    #     if node.left is None and node.right is None:
    #         return node

    #     if node.left is not None and node.right is not None:
    #         left = find_smallest(node.left)
    #         right = find_smallest(node.right)

    #         if left.val <= right.val:
    #             return left
    #         else:
    #             return right

    #     if node.left is not None:
    #         return find_smallest(node.left)

    #     if node.right is not None:
    #         return find_smallest(node.right)

    # return find_smallest(arr)
    # a = 4
    # b = 2
    # a, b = b, a
    # return a, b

    # def swap(self, a, b):
    #     a, b = b, a
    #     return a, b
    # a = 4
    # b = 2
    # a, b = self.swap(a, b)
    # return a, b
    # a, b = b, a
    # return a, b
    # a = 4
    # b = 2
    # a = b
    # return a, b

    def swap(self, a, b):
        a, b = b, a
        return a, b

    a = 4
    b = 2
    a, b = swap(a, b)
    return a, b

