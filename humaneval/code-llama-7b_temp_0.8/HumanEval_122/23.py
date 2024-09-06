
def add_elements(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

        Input: arr = [111,21,3,4000,5,6,7,8,9], k = 4
        Output: 24 # sum of 21 + 3

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    """

    """ALGORITHM"""
    ## INITIALIZE VARS ##

    # create a window (heap) of size k
    # add elements from arr into the window (heap)
    # calculate sum of elements in the window

    window_arr = []
    sum_arr = 0
    ## Create Window Array
    for i in range(k):
        window_arr.append(arr[i])
    ## Sum up elements in the window
    for i in range(len(window_arr)):
        sum_arr += window_arr[i]
    ## STEP THROUGH ARRAY
    for i in range(k, len(arr)):
        ## FIRST ELEMENT OF WINDOW, DELETE FROM HEAP
        sum_arr -= window_arr[0]
        window_arr.pop(0)
        ## ADD NEXT ELEMENT TO HEAP
        window_arr.append(arr[i])
        sum_arr += window_arr[len(window_arr) - 1]

    return sum_arr
