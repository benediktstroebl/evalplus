
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
    if k == 0:
        return 0
    arr.sort()
    for i in range(0, k):
        if i!= 0:
            arr[i] += arr[i - 1]
    new_arr = [0] * k
    new_arr[0] = arr[0]
    for i in range(1, k):
        new_arr[i] = new_arr[i - 1] * 10 + arr[i]
    return sum(new_arr
