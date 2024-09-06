
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
    # # Version 1:
    # # Step 1: we will create a variable `even_array` which will store only the even elements from the array `arr`.
    # even_array = [item for item in arr if item % 2 == 0]
    # # Step 2: if the `even_array` is empty, we will return an empty list, otherwise, we will continue.
    # if len(even_array) == 0:
    #     return []
    # # Step 3: we will sort the `even_array` in ascending order.
    # even_array.sort()
    # # Step 4: we will find the first even element which is an even number.
    # smalest_even_number = even_array[0]
    # # Step 5: we will return a list with the even number and the index of that even number.
    # return [smalest_even_number, arr.index(smalest_even_number)]
    # # # Version 2:
    # # # Step 1: we will create a variable `even_array` which will store only the even elements from the array `arr`.
    # even_array = [item for item in arr if item % 2 == 0]
    # # Step 2: if the `even_array` is empty, we will return an empty list, otherwise, we will continue.
    # if len(even_array) == 0:
    #     return []
    # # Step 3: we will sort the `even_array` in ascending order.
    # even_array.sort()
    # # Step 4: we will find the first even element which is an even number.
    # smalest_even_number = even_array[0]
    # # Step 5: we will find the index of that even number.
    # index_of_even_number = arr.index(smalest_even_number)
    # # Step 6: we will return a list with the even number and the index of that even number.
    # return [smalest_even_number, index_of_even_number]
    # # Version 3:
    # if
