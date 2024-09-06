
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
    # https://www.educative.io/courses/grokking-the-coding-interview/Y1VObN21u4l

    # create a new list to store the elements with at most two digits
    new_arr = []

    # iterate through the first k elements
    for i in range(k):
        if len(str(arr[i])) <= 2:
            new_arr.append(arr[i])

    return sum(new_arr)

