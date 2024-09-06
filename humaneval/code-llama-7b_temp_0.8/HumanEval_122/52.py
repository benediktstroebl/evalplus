
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
    num_of_digits = 0

    for i in range(len(arr)-k):
        # check number of digits
        if arr[i] >= 10:
            num_of_digits += 2
        else:
            num_of_digits += 1
        
        # if number of digits < 3, add to total
        if num_of_digits <= 2:
            total += arr[i]

    # add the last k elements
    for i in range(len(arr)-k, len(arr)):
        total += arr[i]

    return total
