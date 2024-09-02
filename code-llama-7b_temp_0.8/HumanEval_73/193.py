
def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    """

    #
    # n = len(arr)
    # if n % 2 == 0:
    #     return n // 2
    # return n // 2 + 1

    #
    # # Variation 1
    # total = 0
    # half = n // 2
    #
    # # Find the smallest 2*half elements
    # for i in range(0, half):
    #     if arr[i] != arr[n-i-1]:
    #         total += 1
    #
    # return total

    # Variation 2
    # left = []
    # right = []
    # n = len(arr)
    # half = n // 2
    #
    # for i in range(0, half):
    #     left.append(arr[i])
    #     right.append(arr[n-i-1])
    #
    # return left.index(max(left)) + right.index(min(right))

    # Variation 3
    # n = len(arr)
    # half = n // 2
    # left = 0
    # right = 0
    #
    # for i in range(0, half):
    #     if arr[i] != arr[n-i-1]:
    #         left += 1
    #         right += 1
    #
    # return left + right

    # Variation 4
    # n = len(arr)
    #
    # # Count the number of elements that are same on both sides
    # for i in range(n // 2):
    #     if arr[i] != arr[n - i - 1]:
    #         return n - i - 1
    # return n // 2

    # Variation 5
    # n = len(arr)
    # half = n // 2
    #
    # # Count the number of elements that are same on both sides
    # for i in range(0, half):
    #     if arr[i] != arr[n - i - 1]:
    #         return n - i - 1
    #
