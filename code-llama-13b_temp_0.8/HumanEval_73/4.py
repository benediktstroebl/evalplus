
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
    # 0. Check if array is already palindromic
    if is_palindromic(arr):
        return 0
    # 1. Find the center of the array
    mid = len(arr) // 2
    # 2. Count the number of items on both sides of the center
    if len(arr) % 2 == 0:
        left_count = mid
        right_count = mid - 1
    else:
        left_count = mid
        right_count = mid
    # 3. Store left and right sides in separate arrays
    left = []
    right = []
    for i in range(left_count):
        left.append(arr[i])
    for i in range(right_count, len(arr)):
        right.append(arr[i])
    # 4. Find the minimum number of changes required to get left and right
    # to match
    left_changes = find_changes(left, "left")
    right_changes = find_changes(right, "right")
    # 5. Return the sum of the changes needed to make the palindromic
    return left_changes + right_changes

