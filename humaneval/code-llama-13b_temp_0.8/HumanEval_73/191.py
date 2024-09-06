
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
    # 1st approach: TLE O(n^2)
    # if not arr:
    #     return 0
    # start, end = 0, len(arr)-1
    # left_half, right_half = [arr[start]], [arr[end]]
    # while left_half[-1] != right_half[-1]:
    #     if left_half[-1] == right_half[-1]:
    #         if left_half[-1] == arr[start] or right_half[-1] == arr[end]:
    #             break
    #     start += 1
    #     end -= 1
    #     left_half.append(arr[start])
    #     right_half.append(arr[end])
    # return len(arr) - len(left_half)

    # 2nd approach: O(n)
    # O(n) time | O(n) space
    if not arr:
        return 0
    arr_len = len(arr)
    left, right = 0, arr_len - 1
    count = 0
    while left <= right:
        if arr[left] != arr[right]:
            count += 1
            if left != right and arr[left + 1] == arr[right]:
                left += 1
            elif right != left and arr[right - 1] == arr[left]:
                right -= 1
            else:
                left += 1
                right -= 1
        else:
            left += 1
            right -= 1
    return count

