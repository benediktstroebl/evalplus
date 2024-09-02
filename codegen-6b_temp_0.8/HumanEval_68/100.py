
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
    result = []

    def find_smallest_even(arr):
        smallest_even = 9999
        smallest_even_val = -1
        smallest_even_index = -1
        for i in range(len(arr)):
            if arr[i] % 2 == 0:
                if smallest_even > arr[i]:
                    smallest_even = arr[i]
                    smallest_even_val = arr[i]
                    smallest_even_index = i
        return [smallest_even_val, smallest_even_index]

    def find_smallest_index(arr):
        smallest_index = 0
        for i in range(len(arr)):
            if arr[smallest_index] > arr[i]:
                smallest_index = i
        return smallest_index

    def find_smallest_odd(arr):
        smallest_odd = 9999
        smallest_odd_val = -1
        smallest_odd_index = -1
        for i in range(len(arr)):
            if arr[i] % 2 != 0:
                if smallest_odd > arr[i]:
                    smallest_odd = arr[i]
                    smallest_odd_val = arr[i]
                    smallest_odd_index = i
        return [smallest_odd_val, smallest_odd_index]

    def find_smallest(arr):
        if len(arr) == 0:
            return []
        smallest_even = find_smallest_even(arr)
        smallest_odd = find_smallest_odd(arr)
        if smallest_even[0] == -1:
            return smallest_odd
        if smallest_odd[0] == -1:
            return smallest_even
        if smallest_even[0] <= smallest_odd[0]:
            return smallest_even
        else:
            return smallest_odd

    if len(arr) == 0:
        return []

    for i in range(len(arr)):
        result.append(find_smallest(arr[i:]))

    if len(result) == 0:
        return []
    t = result.pop