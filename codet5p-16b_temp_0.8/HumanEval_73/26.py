
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

    left_half = arr[:len(arr)//2]
    right_half = arr[len(arr)//2:]
    left_half_count = 0
    right_half_count = 0
    count = 0

    for i in range(len(arr)):
        if left_half[i] == right_half[i]:
            continue
        else:
            if left_half[i]!= right_half[i - 1]:
                count += 1
            if left_half[i]!= right_half[i]:
                count += 1
            left_half_count += 1
            right_half_count += 1
    return count

