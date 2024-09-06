
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
    # Base case
    if k == 0:
        return 0

    # If an element is less than 100 then the two digits is true
    if arr[k-1] < 100:
        return arr[k-1]

    # Else check if the next element is less than 100
    elif arr[k-2] < 100:
        return arr[k-2]

    # Else the return the sum of the two element with more than 2 digits
    else:
        return arr[k-2] + arr[k-1]

