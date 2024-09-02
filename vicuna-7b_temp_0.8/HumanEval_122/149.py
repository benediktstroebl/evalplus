
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
    # create a new array for the output result
    result = [0] * 10
    for i in range(1, len(arr)):
        # if the number of digits in the current element is <= 2, add the current element to the result array
        if len(str(arr[i])) <= 2:
            result[arr[i]-'0'] += arr[i]
    # sort the result array
    result = sorted(result)
    # return the sum of the elements in the first k positions of the result array
    return sum(result[:k])