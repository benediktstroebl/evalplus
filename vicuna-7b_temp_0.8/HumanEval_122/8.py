
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
    # build the left, middle, and right sum
    left = 0
    middle = 0
    right = 0
    for i in range(0, len(arr), k):
        left = arr[i]
        for j in range(i+1, len(arr), k):
            middle = arr[j]
        right = arr[i+1]
        if len(str(left)) <= 2 or len(str(middle)) <= 2 or len(str(right)) <= 2:
            # add up the middle sum
            sum = left + middle + right
            # add up the left and right sum if there are three digits in the array
            if len(str(left)) <= 2 and len(str(right)) <= 2:
                sum += left
                sum += right
    return sum