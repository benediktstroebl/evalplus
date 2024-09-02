
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
    left = 0
    right = 0
    middle = 0

    for i in range(k, len(arr)):
        if arr[i] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            while left < i:
                right = arr[left] + arr[right]
                left += 1
            middle = (left - 1) // 2
            right = middle + (arr[middle] - 48)
            right = str(right)
            if len(right) == 1:
                right = "0" + right
            if len(right) == 2:
                right = "0" + right
            arr[i-1] = right
            left = middle + 1
        else:
            arr[i-1] += arr[i]

    return arr