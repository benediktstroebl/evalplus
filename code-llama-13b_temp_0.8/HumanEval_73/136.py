
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
    if len(arr) < 2:
        return 0
    
    left, right = 0, len(arr) - 1
    min_changes = 0
    while left <= right:
        if arr[left] != arr[right]:
            # the 2 elements do not match, so we need to decide if to change the left
            # or right element. The right element can only be changed to the left element.
            # we need to find the smallest cost:
            # if we change the left element to the right element, we need to change
            # the right element to the left element (if it does not already match the
            # left element).
            left_to_right = right + 1
            while left_to_right <= len(arr) - 1 and arr[left_to_right] != arr[left]:
                left_to_right += 1
            # print(left_to_right, left, arr)
            if left_to_right == len(arr):
                # if we can't change the right element to the left, we need to change
                # the left element to the right element.
                min_changes += 1
                left += 1
            else:
                # since the right element can be changed to the left element, we can
                # change the left element to the right element, then change the right
                # element to the left element.
                min_changes += 2
                left_to_right += 1
        else:
            left += 1
        right -= 1
    return min_changes
