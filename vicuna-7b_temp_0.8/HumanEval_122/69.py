
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
    arr_copy = [x for x in arr]
    count = 0
    for i in range(k, len(arr_copy)):
        count += int(arr_copy[i])
    for i in range(k, len(arr_copy)):
        arr_copy[i] = str(count)
        count = 0
        for j in range(k, len(arr_copy)):
            count += int(arr_copy[j])
    return sum(int(x) for x in arr_copy[:k])
