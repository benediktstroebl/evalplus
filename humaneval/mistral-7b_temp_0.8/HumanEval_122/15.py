
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
    # Solution 1: Iterate through arr to get the sum of the elements
    # with at most two digits and add the first k elements to the sum
    sum = 0
    for i in range(k):
        num = arr[i]
        if len(str(num)) > 2:
            continue
        else:
            sum += num

    # Solution 2: Get the sum of the first k elements and add the elements with at most two digits
    # to the sum
    sum = sum(arr[:k])
    for num in arr[k:]:
        if len(str(num)) > 2:
            continue
        else:
            sum += num

    # Solution 3: Use a set to remove the elements with more than two digits
    # and get the sum of the remaining elements
    sum = sum(set(arr[:k]))
    for num in arr[k:]:
        if len(str(num)) > 2:
            continue
        else:
            sum += num

    return sum
