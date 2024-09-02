
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
    if k > n:
        return 0
    sum = 0
    for i in range(k):
        digit1,digit2 = map(int,arr[i:i+2])
        if len(str(digit1)) > 1:
            digit1 = digit1 // 10**(len(str(digit1))-1)
        if len(str(digit2)) > 1:
            digit2 = digit2 // 10**(len(str(digit2))-1)
        sum += int(digit1) + int(digit2)
    return sum
