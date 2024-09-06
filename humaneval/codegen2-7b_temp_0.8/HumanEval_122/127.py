
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
    start, end = 0, len(arr)
    while start < end:
        lowest = arr[start]
        start += 1
        while start < end:
            if arr[start] > 9:
                lowest = min(lowest, arr[start] * 10)
            start += 1
        high = 0
        while end > start:
            if arr[end - 1] > 9:
                high += arr[end - 1] - 9
            end -= 1
        if high > k - 1:
            return lowest + high
        else:
            
