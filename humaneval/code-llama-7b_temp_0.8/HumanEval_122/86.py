
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
    # A: keep a window of k elements of the array
    window = arr[:k]

    # B: calculate the sum of the window
    sum_window = sum(window)

    # C: iterate over the rest of the array
    for i in range(k, len(arr)):
        sum_window -= window.pop(0)
        sum_window += arr[i]
        # D: add the current window sum to result
        #    if window length > 2 digits
        #    else continue
        if len(str(sum_window)) > 2:
            return sum_window

    # E: return the final result
    return sum_window

