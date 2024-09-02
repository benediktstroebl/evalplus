
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

    if not arr or k <= 0:
        return 0
    # create a set that stores the last two digits of each element
    subsum = set()
    # initialize the sum of elements with at most two digits
    res = 0
    for i in range(k):
        # create a variable that stores the last two digits of current element
        sub = arr[i] % 100
        # if it already exists in the set, increase the sum by that element
        if sub in subsum:
            res += arr[i]
        # otherwise, add that element to the set
        else:
            subsum.add(sub)
    return res

