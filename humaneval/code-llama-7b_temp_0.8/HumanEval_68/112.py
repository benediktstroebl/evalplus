
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
    odd = []
    even = []

    for index, value in enumerate(arr):
        if value % 2 == 0:
            even.append(value)
        else:
            odd.append(value)

    # if even and odd are empty then return empty list
    if not even and not odd:
        return []

    # if even are empty, return odd smallest value and index
    if not even:
        return [odd[0], odd.index(odd[0])]

    # if even are present, get the smallest even value and index
    even_smallest = min(even)
    even_index = arr.index(even_smallest)

    # if there are no odd values, return even smallest value and index
    if not odd:
        return [even_smallest, even_index]

    # if there are odd values, return the smaller even value and index
    odd_smallest = min(odd)

    if odd_smallest < even_smallest:
        return [odd_smallest, arr.index(odd_smallest)]
    else:
        return [even_smallest, even_index]
