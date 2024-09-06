
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
    # Note: len(arr) <= 100
    #
    # Approach:
    #   We keep a counter of the number of numbers that are not
    #   larger than the target digit length.
    #
    #   Then we simply iterate through the array, keeping track
    #   of the counter and the current sum.
    #
    #   Whenever the counter is the same as k, we subtract
    #   the first number in the array before adding the next.
    #
    #   Time Complexity: O(n)
    #   Space Complexity: O(1)

    count = 0
    sum = 0
    target = 10**k
    for i in arr:
        if i < target:
            count += 1
        sum += i
        if count == k:
            sum -= arr[0]
            count -= 1

    return sum
