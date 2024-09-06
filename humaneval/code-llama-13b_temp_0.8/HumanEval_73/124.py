
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
    changes = 0
    max_len = len(arr)

    if max_len < 2:
        return 0

    is_paldromic = False
    for i in range(0, int(max_len / 2)):
        if arr[i] != arr[max_len - i - 1]:
            is_paldromic = False
            break
        else:
            is_paldromic = True

    if is_paldromic:
        return 0

    left = 0
    while left < max_len / 2 and is_paldromic:
        if arr[left] != arr[max_len - left - 1]:
            is_paldromic = False
            break
        else:
            is_paldromic = True
        left += 1

    right = max_len - 1
    while right > max_len / 2 and is_paldromic:
        if arr[right] != arr[max_len - right - 1]:
            is_paldromic = False
            break
        else:
            is_paldromic = True
        right -= 1

    if not is_paldromic:
        return -1

    left_changes = 0
    while left < max_len / 2:
        if arr[left] != arr[max_len - left - 1]:
            left_changes += 1
        left += 1
    changes += left_changes

    right_changes = 0
    while right > max_len / 2:
        if arr[right] != arr[max_len - right - 1]:
            right_changes += 1
        right -= 1
    changes += right_changes

    return changes
