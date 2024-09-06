
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
    # convert arr to list
    arr = [i for i in arr]
    # initialize the sum to 0
    sum = 0
    # initialize a counter variable for keeping track of the number of elements with at most 2 digits
    count = 0
    # iterate through the first k elements of arr
    for i in range(k, len(arr)):
        # if the current element has at most 2 digits, add it to the sum
        if len(str(arr[i])) <= 2:
            sum += arr[i]
            # increment the counter variable
            count += 1
        # if the counter variable is greater than k, we have summed enough elements
            # and return the sum
            if count >= k:
                return sum
    # if we have not summed enough elements, return -1
    return -1