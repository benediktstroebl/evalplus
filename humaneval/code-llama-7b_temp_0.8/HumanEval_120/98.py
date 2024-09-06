
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
    # initialize an empty list to hold our results
    res = []

    # use a for loop to iterate over the list
    for _ in range(k):

        # initialize the largest to a large number
        largest = -99999999

        # use a for loop to iterate over the list
        for i in range(len(arr)):

            # if the current value is greater than the largest, update largest
            if arr[i] > largest:
                largest = arr[i]

        # after iterating over the list, append the largest to the results list
        res.append(largest)

        # use a for loop to iterate over the list
        for i in range(len(arr)):

            # if the current value is equal to largest, update the array with -99999999
            if arr[i] == largest:
                arr[i] = -99999999

    return res
