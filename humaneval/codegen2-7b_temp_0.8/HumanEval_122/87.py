
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
    
    total = 0
    for i in range(k):
        total += int(arr[i])

    digit1_sum = 0
    digit2_sum = 0
    for i in range(k, len(arr)):
        current = int(arr[i])
        if len(str(current)) == 2:
            digit1_sum += current
        else:
            digit2_sum += current
        if len(digit1_sum + digit2_sum) > total:
            total = digit1_sum + digit2_sum

    return
