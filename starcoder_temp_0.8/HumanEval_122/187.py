
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
    # # Time Complexity: O(n)
    # # Space Complexity: O(1)
    # # n is the length of arr
    # res = 0
    # for i in range(k):
    #     res += arr[i]

    # return res % 10000

    # # Time Complexity: O(n)
    # # Space Complexity: O(1)
    # # n is the length of arr
    # if k < 2:
    #     return 0

    # total_sum = 0
    # for i in range(k):
    #     total_sum += arr[i]

    # return total_sum % 10000

    # # Time Complexity: O(n)
    # # Space Complexity: O(1)
    # # n is the length of arr
    # if k < 2:
    #     return 0

    # arr.sort(reverse=True)
    # return (sum(arr[:k]) % 10000)

    # # Time Complexity: O(n)
    # # Space Complexity: O(1)
    # # n is the length of arr
    # if k < 2:
    #     return 0

    # arr.sort(reverse=True)
    # total_sum = 0
    # for i in range(k):
    #     total_sum += int(str(arr[i])[-2:])

    # return total_sum % 10000

    # # Time Complexity: O(n)
    # # Space Complexity: O(1)
    # # n is the length of arr
    # if k < 2:
    #     return 0

    # arr.sort(reverse=True)
    # total_sum = 0
    # for i in range(k):
    #     if len(str(arr[i])) > 1:
    #         total_sum += int(str(arr[i])[-2:])

    # return total_sum % 10000

    # # Time Complexity: O(n)
    # # Space Complexity: O(n)
    # # n is the length of arr
    # if k < 2:
    #     return 0

    # arr.sort(reverse=True)
    # res = [0 for i in range
