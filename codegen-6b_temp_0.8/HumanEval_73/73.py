
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
    arr_len = len(arr)
    # Base case. This is to catch the single element case
    if arr_len == 1:
        return 0

    middle = arr_len // 2
    middle_val = arr[middle]
    if is_palindrome(arr):
        return 0
    left_count = middle_count = right_count = 0
    for i in range(middle):
        # We need to check that the element we're changing is the same as the one we're changing to
        # This is because we can't change to a different element than that
        if arr[middle-i-1] == middle_val:
            left_count += 1
        else:
            break

    for i in range(middle+1, arr_len):
        if arr[i] == middle_val:
            right_count += 1
        else:
            break

    left_count += middle_count

    return left_count + right_count

assert(smallest_change([1,2,3,5,4,7,9,6]) == 4)
assert(smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1)
assert(smallest_change([1, 2, 3, 2, 1]) == 0)
assert(smallest_change([1, 1, 2, 3, 4, 4]) == 2)
assert(smallest_change([5, 5, 5, 5, 5, 5, 5]) == 0)
assert(smallest_change([1, 5, 1, 5, 1]) == 2)
