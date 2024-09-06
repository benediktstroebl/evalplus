
def maximum(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the maximum k numbers in arr.

    Example 1:

        Input: arr = [-3, -4, 5], k = 3
        Output: [-4, -3, 5]

    Example 2:

        Input: arr = [4, -4, 4], k = 2
        Output: [4, 4]

    Example 3:

        Input: arr = [-3, 2, 1, 2, -1, -2, 1], k = 1
        Output: [2]

    Note:
        1. The length of the array will be in the range of [1, 1000].
        2. The elements in the array will be in the range of [-1000, 1000].
        3. 0 <= k <= len(arr)
    """
    def maximum_helper(arr, k):
        """
        Helper function that returns the k maximum numbers in a list.
        If k < 0, then return the array in descending order.
        If k > len(array), then return the array in ascending order.
        """
        if k < 0:
            return arr[::-1]
        if k > len(arr):
            return arr

        front, back = 0, len(arr) - 1
        while front <= back:
            index = random.randint(front, back)
            arr[index], arr[front] = arr[front], arr[index]
            front += 1
        
        return arr

    return maximum_helper(arr, k)

