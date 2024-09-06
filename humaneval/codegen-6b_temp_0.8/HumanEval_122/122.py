
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
    ## Time Complexity: O(n**2)
    # result = 0
    # for i in range(len(arr)):
    #     for j in range(i, i+k):
    #         result += arr[j]
    # return result

    ## Time Complexity: O(n)
    # result = 0
    # for i in range(len(arr)):
    #     if i < k:
    #         result += sum(arr[:i+1])
    #     else:
    #         result += sum(arr[i-k+1:i+1])
    # return result

    ## Time Complexity: O(n)
    result = sum(arr[:k])
    result += sum(arr[k:])
    return result

