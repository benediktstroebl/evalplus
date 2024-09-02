
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
    def _pluck(arr):
        nodes = [val for val in arr if val != 0]
        if nodes:
            even_nodes = [node for node in nodes if node % 2 == 0]
            indices = [node for node in nodes if node % 2 != 0]
            if even_nodes:
                return [min(even_nodes), min(indices)]
            return [None, None]
        return [None, None]


    def _pluck_slow(arr):
        """
        Algorithm: 
            Set the smallest node to a variable, and set two pointers
            pointer_start, pointer_end, starting from the very beginning of the array.
            While pointers_end < len(arr)
                If arr[pointer_end] is even
                    set the smallest to arr[pointer_end]
                    increment pointers_end
                else
                    set the smallest to arr[pointer_start]
                    update pointers_start
                increment pointers_end
        Return the pointers_start and pointers_end
        """
        nodes = [val for val in arr if val != 0]
        if nodes:
            indices = [node for node in nodes]
            indices.sort()
            smallest = indices[0]
            pointer_start = smallest
            pointer_end = smallest + 1
            while pointer_end < len(arr):
                if arr[pointer_end] % 2 == 0:
                    smallest = arr[pointer_end]
                    pointer_end += 1
                else:
                    smallest = arr[pointer_start]
                    pointer_start += 1
            return [pointer_start, pointer_end]
        return [None, None]

    def _pluck_in_place(arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        nodes = [val for val in arr if val != 0]
        if len(nodes) < 1:
            return []
        node_min = nodes[0]
        for node in nodes[1:]:
            if node < node_min:
                node_min = node
        i = arr.index(node_min)