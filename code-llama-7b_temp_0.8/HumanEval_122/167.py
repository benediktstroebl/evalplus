
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
    if len(arr) <= k:
        return sum(arr)

    target = sum(arr[:k])
    print(target)
    i = 0
    while i < len(arr):
        if len(str(arr[i])) <= 2:
            i += 1
        else:
            target -= arr[i]
            k -= 1
            if k == 0:
                break
            arr[i] = 0
    return target

