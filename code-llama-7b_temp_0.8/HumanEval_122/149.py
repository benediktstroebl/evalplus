
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

    def check_k_elements(index, k, sum):
        if index >= len(arr):
            return sum
        else:
            if len(str(arr[index])) <= 2:
                k -= 1
                if k == 0:
                    return sum + arr[index]
                else:
                    return check_k_elements(index + 1, k, sum + arr[index])
            else:
                return check_k_elements(index + 1, k, sum)

    return check_k_elements(0, k, 0)

