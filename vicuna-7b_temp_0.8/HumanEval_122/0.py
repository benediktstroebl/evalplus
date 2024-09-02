
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
    n = len(arr)
    if n == 0:
        return 0
    for i in range(1, k):
        j = (n-i)//2
        arr_1 = arr[:j+1]
        arr_2 = arr[j+1:]
        sum = 0
        for i in arr_1:
            sum += int(i)
        for i in arr_2:
            if i.isdigit() and len(str(i)) <= 2:
                sum += int(i)
        if k != j+1:
            arr[j] += sum
    return 0