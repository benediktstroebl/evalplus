
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
    # 1st brute force solution
    # import re
    # return sum([sum(map(int, re.findall(r"\d{1,2}", str(x)))) for x in arr[:k]])
    # 2nd solution
    count = 0
    for i in range(k):
        x = str(arr[i])
        if len(x) > 2:
            count += int(x[0]) + int(x[-1])
        else:
            count += int(x)
    return count

