
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
    # This is a tricky one!
    # 1. Iterate through arr starting from the 1st element.
    # 2. If the length of the number is <= 2,
    #    add it to the running total.
    # 3. Stop once you reach k, or when the number of digits > 2
    # 4. Return the running total.
    #
    # Time Complexity: O(n), where n = len(arr)
    # Space Complexity: O(1), constant space used

    running_total = 0
    for i in range(len(arr)):
        if len(str(arr[i])) <= 2:
            running_total += arr[i]
        if i >= k:
            break

    return running_total

