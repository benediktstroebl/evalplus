
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
    # Boundary conditions
    if len(arr) == 0:
        return 0
    if k == 0:
        return 0
    if k == 1:
        return arr[0]

    # We know that we have less than 100 values.
    # So we can represent them using one digit.
    if arr[k - 1] < 10:
        return sum(arr[:k])

    # We have k >= 2.
    # So, we will consider the last k - 1 values as an array.
    # Now, we can find the first k - 2 values of the array.
    # We don't need to consider k - 2 because its first element is bigger than 10.
    if arr[k - 2] < 10:
        return sum(arr[:k]) - arr[k - 2]

    # We have k >= 3.
    # So, we will consider the last k - 2 values as an array.
    # Now, we can find the first k - 3 values of the array.
    # We don't need to consider k - 3 because its first element is bigger than 10.
    if arr[k - 3] < 10:
        return sum(arr[:k]) - arr[k - 2] - arr[k - 3]

    # We have k >= 4.
    # So, we will consider the last k - 3 values as an array.
    # Now, we can find the first k - 4 values of the array.
    # We don't need to consider k - 4 because its first element is bigger than 10.
    if arr[k - 4] < 10:
        return sum(arr[:k]) - arr[k - 2] - arr[k - 3] - arr[k - 4]

    # If we got here, all elements of the array is bigger than 10.
    # So, we can just find the first k - 5 values of the array.
    return sum(arr[:k]) - arr[k - 2] - arr[k - 3] -
