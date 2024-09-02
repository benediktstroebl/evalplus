
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
    arr = list(arr)
    k = int(k)
    left = 0
    right = 1
    while right < k:
        if len(arr) == 0:
            break
        middle = (left + right) // 2
        sum = arr[left] + arr[middle] + arr[right]
        right = middle + 1
        left = middle + 1
        if len(arr) > 1 and (sum // 10) == (arr[1] // 10):
            sum = (sum - arr[0] * 10) + arr[1]
            arr.insert(left, arr[1])
            arr.pop(right)
            left = middle + 1
            right = middle + 1
        elif len(arr) > 1 and (sum // 10) == (arr[1] // 10):
            sum = (sum - arr[0] * 10) + arr[1]
            arr.insert(left, arr[0])
            arr.insert(middle, arr[1])
            arr.pop(right)
            left = middle + 1
            right = middle + 1
        else:
            if len(arr) > 1 and (sum // 10) == (arr[0] // 10):
                sum = (sum - arr[0] * 10) + arr[1]
                arr.insert(left, arr[0])
                arr.pop(right)
                left = middle + 1
                right = middle + 1
            else:
                break
    return sum



Example:

input = [111,21,3,4000,5,6,7,8,9]
