
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

    # A: store the sum of the first k numbers
    curr_sum = sum(arr[0:k])

    # B: iterate through the first k elements of the array
    for i in range(k):

        # C: if the number's digit is 1, then it is a valid number
        if len(str(arr[i])) == 1:

            # D: if the number is valid, add it to the current sum
            curr_sum += arr[i]

            # E: remove the number from the array
            arr.remove(arr[i])

            # F: reset i
            i -= 1

        # G: else, it's a number with more than 1 digits
        else:
            # H: remove the number from the array
            arr.remove(arr[i])

            # I: reset i
            i -= 1

    return curr_sum

