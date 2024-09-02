
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

    arr = [str(x) for x in arr] # convert list of integers to list of strings

    sum = 0

    for i in range(k): # loop over the first k elements of the array

        if len(arr[i]) <= 2: # if the length of the string is 2 or less
            sum += int(arr[i]) # add the integer value to the sum

    return sum

