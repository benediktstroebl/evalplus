
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
    if len(arr) <= 100:
        while len(arr) > 0:
            if len(arr) % 10 == 0:
                sum = arr.pop(0)
                if k < sum:
                    k += 10
            if len(arr) % 10 != 0:
                sum = 0
                for i in range(len(arr)):
                    if len(arr[i]) <= 2:
                        sum += arr[i]
                arr.pop(0)
                break
        return sum
    else:
        return 0