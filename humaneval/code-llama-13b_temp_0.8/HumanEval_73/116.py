
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

    # if len(arr) == 0:
    #     return 0
    #
    # if len(arr) == 1:
    #     return 0
    #
    # half = len(arr) // 2
    # if len(arr) % 2 == 0:
    #     right = half - 1
    # else:
    #     right = half
    #
    # left = 0
    # change = 0
    # while right >= 0:
    #     if arr[left] != arr[right]:
    #         change += 1
    #         arr[right] += 1
    #         arr[left] -= 1
    #     right -= 1
    #     left += 1
    #
    # return change

    n = len(arr)
    front = [1] * n
    back = [1] * n

    front[0] = arr[0]
    for i in range(1, n):
        front[i] = front[i - 1] + arr[i]

    back[-1] = arr[-1]
    for i in range(1, n):
        back[-i - 1] = back[-i] + arr[-i - 1]

    change = 0
    for i in range(n - 1):
        change += min(front[i], back[i + 1]) - arr[i]

    return change

