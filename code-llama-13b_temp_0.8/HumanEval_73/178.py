
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
    if not arr or len(arr) == 0:
        return 0
    if len(arr) == 1:
        return 0

    n = len(arr)

    # Find the index at which the array becomes not palindromic
    # By doing this we will know the length of the substring that we need to change
    # For example:
    # [1, 2, 3, 5, 4, 7, 9, 6]
    #      ^
    # [1, 2, 3, 4, 3, 2, 2]
    #       ^
    # [1, 2, 3, 2, 1]
    #   ^
    #
    # By doing this we will also know the side of the array that we need to calculate the distance
    # For example:
    # [1, 2, 3, 5, 4, 7, 9, 6]
    #      ^
    # [1, 2, 3, 4, 3, 2, 2]
    #       ^
    # [1, 2, 3, 2, 1]
    #     ^

    # First we check the first half
    l = 0
    r = n - 1
    while l < r:
        if arr[l] != arr[r]:
            break
        l += 1
        r -= 1
    change_range = r - l + 1
    if l == r:
        return 0

    # Now we check the second half
    l = n - 1
    r = n - change_range - 1
    while l > r:
        if arr[l] != arr[r]:
            break
        l -= 1
        r += 1

    return change_range + (l - r + 1)
