
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
    def digits(arr, k):
        """
        given an array, return number of digits that are present in array
        """
        count = 0
        for i in range(k):
            count += len(str(arr[i]))
        return count

    n = len(arr)
    # corner case: k > n
    if k > n:
        k = n

    # if array contains all single digit elements then no two digits have to be added
    if digits(arr, k) == k:
        return sum(arr[:k])

    return sum(arr[:k]) + sum(arr[k:])
