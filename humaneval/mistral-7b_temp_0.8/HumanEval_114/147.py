import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # 331. Verify Preorder Serialization of a Binary Tree
    # def isValidSerialization(preorder: str) -> bool:
    #     """
    #     Return True if a given tree is valid, and False otherwise.
    #     Each node of the tree has node.val == 0 or node.val == 1.
    #     The serialization of a tree consists of a list where the elements are
    #     separated by commas (,) and each element (except the last element) is a
    #     pair of values as follows:
    #     - [node_value, node_left_child_value, node_right_child_value]
    #     """
    #     if preorder == '#':
    #         return True
    #     node_value, node_left_child_value, node_right_child_value = preorder.split(',')
    #     return (node_value == '1' and (node_left_child_value == '#' and node_right_child_value == '#')) or
    #             (node_value == '0'
