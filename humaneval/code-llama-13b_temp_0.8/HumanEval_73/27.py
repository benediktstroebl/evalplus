
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
    if len(arr) <= 2:
        return 0
    count_left_half = {}
    count_right_half = {}

    for i in range(len(arr)//2):
        left = arr[i]
        right = arr[len(arr)-i-1]
        if left in count_right_half:
            count_right_half[left] += 1
        else:
            count_right_half[left] = 1
        if right in count_left_half:
            count_left_half[right] += 1
        else:
            count_left_half[right] = 1
    # print(count_left_half, count_right_half)
    odd_count = 0
    for key in count_left_half:
        if key in count_right_half:
            if count_left_half[key] > count_right_half[key]:
                odd_count += count_left_half[key] - count_right_half[key]
            elif count_right_half[key] > count_left_half[key]:
                odd_count += count_right_half[key] - count_left_half[key]
        else:
            odd_count += count_left_half[key]
    for key in count_right_half:
        if key not in count_left_half:
            odd_count += count_right_half[key]
    return odd_count


