
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
    # FIND the node with smallest even value
    # FIND the index of smallest even value
    # RETURN the node with smallest even value and its index
    # If there are no even values, return []
    # If the given array is empty, return []

    # O(n) time | O(1) space - where n is the length of the input array
    # O(n) time | O(1) space
    # if not arr:
    #     return []

    # smallest_even_value = None
    # smallest_even_index = None
    # smallest_even_index_count = None

    # for idx, num in enumerate(arr):
    #     if num % 2 == 0:
    #         if smallest_even_value is None:
    #             smallest_even_value = num
    #             smallest_even_index = idx
    #             smallest_even_index_count = 1
    #         elif num <= smallest_even_value:
    #             smallest_even_value = num
    #             smallest_even_index = idx
    #             smallest_even_index_count = 1
    #         else:
    #             smallest_even_index_count += 1

    # if smallest_even_value is None:
    #     return []

    # return [smallest_even_value, smallest_even_index]


    # O(n) time | O(1) space - where n is the length of the input array
    # O(n) time | O(1) space
    # if not arr:
    #     return []

    # smallest_even_value = None
    # smallest_even_index = None

    # for idx, num in enumerate(arr):
    #     if num % 2 == 0:
    #         if smallest_even_value is None or num < smallest_even_value:
    #             smallest_even_value = num
    #             smallest_even_index = idx

    # return [smallest_even_value, smallest_even_index]


    # O(n) time | O(1) space - where n is the length of the
